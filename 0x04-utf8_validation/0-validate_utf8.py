#!/usr/bin/python3
"""
    This module is a solution to the UTF-8 validation project
"""


def validUTF8(data):
    """
        a method that determines if a given data set
        represents a valid UTF-8 encoding

        Returns:
            True - if data is a valid UTF-8 encoding
            else - false
    """
    num_bytes_to_follow = 0

    for byte in data:
        if num_bytes_to_follow == 0:
            if byte & 0b10000000 == 0:
                num_bytes_to_follow = 0
            elif byte & 0b11100000 == 0b11000000:
                num_bytes_to_follow = 1
            elif byte & 0b11110000 == 0b11100000:
                num_bytes_to_follow = 2
            elif byte & 0b11111000 == 0b11110000:
                num_bytes_to_follow = 3
            else:
                return False
        else:
            if not (byte & 0b11000000 == 0b10000000):
                return False
            num_bytes_to_follow -= 1

            if num_bytes_to_follow < 0:
                return False

    return num_bytes_to_follow == 0
