import os
import numpy as np
from PIL import Image


def mask_to_rle(mask):
    """
    Convert a binary mask to RLE format.
    :param mask: numpy array, 1 - mask, 0 - background
    :return: RLE string
    """
    pixels = mask.T.flatten()
    pixels = np.concatenate([[0], pixels, [0]])
    runs = np.where(pixels[1:] != pixels[:-1])[0] + 1
    runs[1::2] -= runs[::2]
    return [int(x) for x in runs]


def convert_folder_to_rle(folder_path):
    """
    Convert all mask images in a folder to RLE format.
    :param folder_path: path to the folder containing mask images
    :return: dictionary with image filenames as keys and RLE array as values
    """
    rle_annotations = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            img_path = os.path.join(folder_path, filename)
            mask = Image.open(img_path)
            mask_array = np.array(mask)
            binary_mask = (mask_array > 0).astype(np.uint8)

            rle_annotations[filename] = {
                "counts": mask_to_rle(binary_mask),
                "height": mask_array.shape[0],
                "width": mask_array.shape[1],
            }
    return rle_annotations
