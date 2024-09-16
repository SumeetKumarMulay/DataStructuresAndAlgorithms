"""
Write a binary search function which accepts a value and an array of sorted integers. It should 
return the index of the value if the value exits else it should return -1. 
"""


def BinarySearch(input: list, value) -> int:
    pointer1 = 0
    pointer2 = len(input) - 1

    def helper(low: int, high: int) -> int:
        mid_val = low + (high - low) // 2
        # NOTE - Here if the if 'low' if greater then 'high' then it means
        # we have gone through the array once. if this chech does not exist
        # we will be in a loop.
        if low >= high:
            return -1
        if value == input[mid_val]:
            return mid_val
        elif value < input[mid_val]:
            return helper(low=low, high=mid_val - 1)
        else:
            return helper(low=mid_val + 1, high=high)

    return helper(low=pointer1, high=pointer2)
