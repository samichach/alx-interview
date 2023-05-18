#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding
    """
    num_byte = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for i in data:

        msk_byte = 1 << 7

        if num_byte == 0:

            while msk_byte & i:
                num_byte += 1
                msk_byte = msk_byte >> 1

            if num_byte == 0:
                continue

            if num_byte == 1 or num_byte > 4:
                return False

        else:
            if not (i & mask1 and not (i & mask2)):
                return False

        num_byte -= 1

    if num_byte == 0:
        return True
    return False
