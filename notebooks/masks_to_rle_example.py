# %%
import json
from pathlib import Path
from utils import convert_folder_to_rle

# %%
GT_IMAGE_DIR = Path("../data/gt")
PREDS_IMAGE_DIR = Path("../data/preds")

# %%
gt_anns = convert_folder_to_rle(GT_IMAGE_DIR)
preds_anns = convert_folder_to_rle(PREDS_IMAGE_DIR)

# %%

with open("../public/ground_truth.json", "w") as f:
    json.dump(gt_anns, f)

with open("../private/ground_truth.json", "w") as f:
    json.dump(gt_anns, f)

# %%

with open("../public/results.json", "w") as f:
    json.dump(preds_anns, f)

with open("../private/results.json", "w") as f:
    json.dump(preds_anns, f)
