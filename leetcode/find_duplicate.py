"""LINK: {https://leetcode.com/problems/find-the-duplicate-number/}"""

from typing import List


def findDuplicate(nums: List[int]) -> int:
    """t"""
    frequency = {}

    for i in range(len(nums)):
        if nums[i] in frequency:
            frequency[nums[i]] += 1
        else:
            frequency[nums[i]] = 1

    for key in frequency.keys():
        value = frequency[key]
        if value != 1:
            return key


def find_duplicates_floyd(nums: List[int]) -> int:
    """t"""
    slow = fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    fast = nums[0]
    while fast != slow:
        slow = nums[slow]
        fast = nums[fast]
    return slow


resu = find_duplicates_floyd(nums=[1, 3, 4, 2, 2])
print(resu)
