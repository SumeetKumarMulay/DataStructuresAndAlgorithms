"""
Write a function which should accept a large list and break it down into smaller lists until 
each on contains 0 or 1 elements each. It should then merge them together to from a sorted list.
"""


def merge_two_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
    """
    This function merges two sorted arrays. 
    Args:
        list1 (list[int]): First sorted array
        list2 (list[int]): Second sorted array

    Returns:
        list[int]: Merged sorted array. 
    """
    final_list: list[int] = []
    pointer_1 = 0
    pointer_2 = 0

    def compare_merge(l1: list[int], l2: list[int]) -> list[int]:
        nonlocal pointer_1
        nonlocal pointer_2
        nonlocal final_list
        while pointer_1 < len(l1) or pointer_2 < len(l2):
            # NOTE: lets break down the conditional statement:
            # The first half of the statement ensure the pointer_1 is less than the lenght of L1
            # the second half checks if we have checked all the values in the l2 if so than we
            # append all the values in l1 to the final_list. The final 'or' statement is checked
            # when pointers 1 and 2 are less than the lenght of l1, l2 the values at positions
            # pointer_1 and pointer_2 are added in correct order. It is '<=' because the two lists
            # can contain same values.
            if pointer_1 < len(l1) and (pointer_2 >= len(l2) or l1[pointer_1] <= l2[pointer_2]):
                final_list.append(l1[pointer_1])
                pointer_1 += 1
            if pointer_2 < len(l2) and (pointer_1 >= len(l1) or l2[pointer_2] <= l1[pointer_1]):
                final_list.append(l2[pointer_2])
                pointer_2 += 1
        return final_list

    return compare_merge(l1=list1, l2=list2)


def merge_sort(input_list=list) -> list:
    """
    This is a merge sort function which taken in an unsorted array and returns a sorted array.

    Args:
        input_list (_type_, optional): This is the unsorted array. 

    Returns:
        list: sorted array. 
    """
    if len(input_list) <= 1:
        return input_list
    mid_point = int(len(input_list) / 2)
    first_half = merge_sort(input_list=input_list[0: mid_point])
    second_half = merge_sort(input_list=input_list[mid_point:])
    return merge_two_sorted_lists(list1=first_half, list2=second_half)
