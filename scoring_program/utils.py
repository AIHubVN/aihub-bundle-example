import numpy as np


def rle_to_mask(rle, height, width):
    """
    Convert RLE string to a binary mask.
    :param rle: RLE string
    :param shape: tuple, shape of the original mask (height, width)
    :return: numpy array, binary mask
    """

    starts, lengths = [np.asarray(x, dtype=int) for x in (rle[0::2], rle[1::2])]
    starts -= 1
    ends = starts + lengths
    mask = np.zeros(height * width, dtype=np.uint8)
    for start, end in zip(starts, ends):
        mask[start:end] = 1
    return mask.reshape((height, width)).T
