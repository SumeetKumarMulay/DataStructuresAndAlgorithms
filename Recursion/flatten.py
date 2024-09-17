"""
Write a function that flattens a list.
"""


def flatten(input_arr: list[int]) -> list[int]:
    """
    using the helper method we can flatten nested lists.
    """
    new_array = []

    def helper(ip: list[int]):
        for values in ip:
            if isinstance(values, list):
                helper(ip=values)
            else:
                new_array.append(values)
        return new_array

    return helper(ip=input_arr)
