"""
Write a function which selects on element called a pivote point and compare other elements to
this point and put them on on the left side if they are less than or on the right side if they
are greater than.
"""


def pivote_helper(input_list: list, start_index: int = None, end_index: int = None):
    """
    This is the pivote helper function which return a pivote point index.

    Args:
        input_list (list): unsorted array. 
        start_index (int, optional): Start index. Defaults to middle value.
        end_index (int, optional): end index. Defaults to len(input_list).
    """
    def swap(input_list: list, left: int, right: int):
        """
        This function swaps elements on left side to elements on the right side.

        Args:
            input_list (list): input array
            left (int): left value index
            right (int): right value index
        """
        temp = input_list[left]
        input_list[left] = input_list[right]
        input_list[right] = temp

    start_index = start_index if start_index is not None else int(
        len(input_list) / 2)
    end_index = end_index if end_index is not None else len(input_list) - 1
    current_pivote_index: int = start_index

    for index in range(start_index + 1, end_index + 1):
        if input_list[start_index] > input_list[index]:
            current_pivote_index += 1
            swap(input_list=input_list, left=current_pivote_index, right=index,)
    swap(input_list=input_list, left=current_pivote_index, right=start_index)
    return current_pivote_index


def quick_sort(input_list: list, left: int = None, right: int = None) -> list:
    """
    This function accepts an unsorted array and returns a sorted arrays. 

    Args:
        input_list (list): Unsorted array. 
        left (int, optional): To slice the list during recursion and 
                            should not be change by the user. Defaults to None.
        right (int, optional): To slice the list during recursion. Not for use 
                            by the user. Defaults to None.

    Returns:
        list: a sorted list. 
    """
    left = left if left is not None else 0
    right = right if right is not None else len(input_list) - 1
    if left < right:
        pivote_index = pivote_helper(
            input_list=input_list, start_index=left, end_index=right)
        # left side of the list
        quick_sort(input_list=input_list, left=left, right=pivote_index - 1)
        # right side sort
        quick_sort(input_list=input_list, left=pivote_index + 1, right=right)
    return input_list
