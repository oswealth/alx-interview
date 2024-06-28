#!/usr/bin/python3

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    :param data: List of integers
    :return: Boolean indicating whether the data is a valid UTF-8 encoding
    """
    n_bytes = 0

    # Masks to check the significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        mask = 1 << 7
        if n_bytes == 0:
            # Count number of leading 1's
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            # If no leading 1's, it's a 1-byte character
            if n_bytes == 0:
                continue

            # UTF-8 characters must be between 2 and 4 bytes
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # For bytes following the leading byte, check if they start with '10'
            if not (num & mask1 and not (num & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0
