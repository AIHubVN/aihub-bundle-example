import sys
import json
import os
from pathlib import Path
from iou_metric import SMAPIoUMetric
from utils import rle_to_mask

W = H = 128

if __name__ == "__main__":
    [_, input_dir, output_dir] = sys.argv
    # input_dir = "public"
    # output_dir = "public"
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)

    submission_dir = input_dir / "res"
    truth_dir = input_dir / "ref"

    # submission_dir = input_dir
    # truth_dir = input_dir

    with open(truth_dir / "ground_truth.json", "r") as f:
        gt = json.load(f)

    with open(submission_dir / "results.json", "r") as f:
        preds = json.load(f)

    if not set(gt.keys()) == set(preds.keys()):
        raise Exception(
            f"The prediction set and the ground truth set do not have the same number of files. Expecting {len(set(gt.keys()))} files from the prediction set."
        )

    evaluator = SMAPIoUMetric()

    for g in gt:
        gt_arr = rle_to_mask(gt[g]["counts"], gt[g]["height"], gt[g]["width"])

        pred_arr = rle_to_mask(
            preds[g]["counts"], preds[g]["height"], preds[g]["width"]
        )

        evaluator.process(input={"pred": pred_arr, "gt": gt_arr})

    metrics = evaluator.compute_metrics(evaluator.results)

    with open(os.path.join(output_dir, "scores.txt"), "w") as output_file:
        for k, v in metrics.items():
            if k in ["aAcc", "mIoU", "mAcc"]:
                output_file.write(f"{k}: {v:.2f}\n")
            else:
                output_file.write(f"{k}: {v*100:.2f}\n")
