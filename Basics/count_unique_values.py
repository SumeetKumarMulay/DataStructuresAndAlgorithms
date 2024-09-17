"""
Write a function which accepts an array which counts all the unqiue values in that array and
returns the count. 
"""

from typing import Optional


def count_unique_values_v1(input_list: list) -> int:
    """Counts the number of unique values in a given list.

    Args:
      input_list: The input list.

    Returns:
      The number of unique values.
    """

    if not input_list:
        return 0

    sorted_list = sorted(input_list)
    unique_count = 1
    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[i - 1]:
            unique_count += 1

    return unique_count


def count_unique_values_v2(input: list) -> Optional[int]:
    """Counts the number of unique values in a given list.

    Args:
      input_list: The input list.

    Returns:
      The number of unique values.
    """
    pointer1 = 0
    pointer2 = 1
    count = 1
    if input:
        sorted_input = sorted(input) if input else []
        while pointer2 < len(sorted_input):
            if sorted_input[pointer1] != sorted_input[pointer2]:
                count += 1
                pointer1 = pointer2
                pointer2 += 1
            else:
                pointer2 += 1
        return count

    else:
        return None
