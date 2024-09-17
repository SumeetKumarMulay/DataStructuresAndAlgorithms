"""
Write a function which accepts a list and a number. The number tell the number of values to
be summed in the array. so for example if the input is [1, 2, 3, 4, 5, 6] and 4 the first 4 
digits in the list should be added then the next four and soo on. Finially it should return 
the max sum.  
"""

def sum_rec(input: list[int]):
    """
    recursive sum
    """
    if not input:
        return 0
    else:
        return input[0] + sum_rec(input[1:])


# def max_sub_array_sum(nums, k):
#   """Finds the maximum sum of a sub_array of size k in a given list.

#   Args:
#     nums: The input list of numbers.
#     k: The size of the sub_array.

#   Returns:
#     The maximum sum of a sub_array of size k.
#   """

#   if len(nums) < k:
#     raise ValueError("k must be less than or equal to the length of the list")

#   current_sum = sum(nums[:k])
#   max_sum = current_sum

#   for i in range(k, len(nums)):
#     current_sum += nums[i] - nums[i - k]
#     max_sum = max(max_sum, current_sum)

#   return max_sum


def max_sub_array_sum(input_list: list[int], windowSize: int) -> int:
    """Finds the maximum sum of a sub_array of size k in a given list.

    Args:
      nums: The input list of numbers.
      k: The size of the sub_array.

    Returns:
      The maximum sum of a sub_array of size k.
    """
    window_size = windowSize
    sum_val = 0
    if window_size < len(input_list):
        for i in range(0, len(input_list)):
            start_val = i
            sub_array = input_list[start_val:window_size]
            new_sum = sum_rec(sub_array)
            if sum_val > new_sum:
                window_size += 1
            else:
                sum_val = new_sum
                window_size += 1
        return sum_val
    else:
        return -1
