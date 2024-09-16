"""
The functions compaires 2 lists. The first list contains a list of numbers. 
The second list should contain a list of numbers which is the squre of numbers in list one. 
if it matches the above 
conditions then "True" is returned else false is returned.
The order should not matter. 
"""

import array


def same(arry1: list[int], arry2: list[int]) -> bool:
    # we need to make sure the len of both list should be same. since reperation is allowed
    if len(arry1) != len(arry2):
        return False
    else:
        # defining 2 counters
        counter1 = {}
        counter2 = {}
        # converting the list to a object or dict for speed. 
        for value in arry1:
            if counter1.get(value):
                counter1[value] += counter1.get(value)
            else:
                counter1[value] = 1

        for value in arry2:
            if counter2.get(value):
                counter2[value] += counter2.get(value)
            else:
                counter2[value] = 1

        # going through the list of objects (counter1) the sq the keys in counter1 
        # checking if they are not there in counter2 and return false 
        # else if check the frequency is the name 
        for key, value in counter1.items():
            if not (key**2 in counter2):
                return False
            if counter2[key**2] != counter1[key]:
                return False
        print(counter1, counter2)
        return True


