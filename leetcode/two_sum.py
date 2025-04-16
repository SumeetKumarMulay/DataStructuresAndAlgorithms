"""Link: {https://leetcode.com/problems/two-sum/}"""

from typing import List


def two_sum(nums=list, target=int):
    """Follow above link to understand question."""
    hashmap = {}

    if target < 0:
        return []

    for values in nums:
        if values < 0:
            return []

    for i in range(len(nums)):
        hashmap[nums[i]] = i

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashmap and hashmap[diff] != i:
            return [i, hashmap[diff]]
    return []


def two_sums(nums=List[int], target=6):
    nums = [3, 2, 4]
    i = 0
    j = len(nums) - 1

    while i < j:
        sum_value = nums[i] + nums[j]
        if sum_value > target:
            j -= 1
        if sum_value < target:
            i += 1
        if sum_value == target:
            return [i, j]
    return []


exp = two_sums()
print(exp)
