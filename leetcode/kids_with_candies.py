"""
There are n kids with candies. You are given an integer array candies, where each candies[i] 
represents the number of candies the ith kid has, and an integer extraCandies, denoting the 
number of extra candies that you have. Return a boolean array result of length n, where result[i]
is true if, after giving the ith kid all the extraCandies, they will have the greatest number of
candies among all the kids, or false otherwise.

NOTE: that multiple kids can have the greatest number of candies.
"""


def kids_with_candies(candies: list[int], extra_candies: int) -> list[bool]:

    op_list = []

    def find_greatest(input_list: list[int]) -> bool:
        return max(input_list)

    def helper(candies: list[int], extra_candies: int, greatest_val: int) -> list[bool]:
        nonlocal op_list
        print(candies)
        if len(candies) == 0:
            return op_list
        comp_val = candies[0] + extra_candies
        if comp_val >= greatest_val:
            op_list.append(True)
            return helper(candies=candies[1:], extra_candies=extra_candies,
                          greatest_val=greatest_val)
        op_list.append(False)
        return helper(candies=candies[1:], extra_candies=extra_candies, greatest_val=greatest_val)
    grt_val = find_greatest(input_list=candies)
    return helper(candies=candies, extra_candies=extra_candies, greatest_val=grt_val)
