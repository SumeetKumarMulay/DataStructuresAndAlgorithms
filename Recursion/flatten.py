from typing import Optional


def flatten(inputArr: list[int]) -> list[int]:
    new_array = []

    def helper(ip: list[int]):
        for values in ip:
            if type(values) == list:
                helper(ip=values)
            else:
                new_array.append(values)
        return new_array

    return helper(ip=inputArr)

