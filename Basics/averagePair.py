"""
Write a function which accepts a list and target value. check if there is one
pair who's avg is equal to target value. 
"""


def averagePair(input_list: list[int], target_value: float) -> bool:
    pointer1 = 0
    pointer2 = len(input_list) - 1
    if len(input_list) == 0:
        return False
    while pointer1 < pointer2:
        sum = input_list[pointer1] + input_list[pointer2]
        avg = sum / 2
        if avg < target_value:
            pointer1 += 1
        elif avg > target_value:
            pointer2 -= 1
        else:
            return True
    return False


