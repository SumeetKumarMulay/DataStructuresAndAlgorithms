"""
Write a function that takes a list of intergers. The function should find a list 
of two values who's some is zero and put them into another list and return it. If there 
are not values in the list who's sum is equal to zero then the function should return 
undefined. 
"""


def sumZero(input=[]) -> list[int]:
    # the standard sorting method is list o(n) so the function is o(n)
    sortedInput = sorted(input) if input else []
    if sortedInput:
        pointerLeft: int = 0
        pointerRight: int = len(sortedInput) - 1
        checkSum = sortedInput[pointerLeft] + sortedInput[pointerRight]
        if checkSum == 0:
            return [sortedInput[pointerLeft], sortedInput[pointerRight]]
        elif checkSum > 0:
            sortedInput.pop(pointerRight)
            return sumZero(input=sortedInput)
        elif checkSum < 0:
            sortedInput.pop(pointerLeft)
            return sumZero(input=sortedInput)
        else:
            return None
    else:
        return None


result = sumZero(
    input=[
        -56,
        32,
        -27,
        78,
        -92,
        3,
        45,
        -17,
        -63,
        71,
        -84,
        25,
        -5,
        97,
        -32,
        66,
        -42,
        15,
        -75,
        89,
        28,
        -10,
        54,
        -67,
        41,
        93,
        -22,
        -8,
        7,
        -52,
        61,
        -37,
        23,
        -98,
        47,
        -1,
        82,
        -4,
        57,
        -73,
        38,
        -24,
        13,
        -94,
        53,
        -68,
        43,
        95,
        -26,
        -9,
        6,
        -51,
        60,
        -36,
        22,
        -99,
        48,
        -2,
        83,
        -5,
        58,
        -74,
        39,
        -25,
        14,
        -96,
        55,
        -69,
        44,
        96,
        -27,
        -11,
        8,
        -50,
        59,
        -35,
        21,
        -100,
        49,
        -3,
        84,
        -54,
        62,
        -38,
        24,
        -97,
        56,
        -70,
        40,
        91,
        -28,
        -12,
        9,
        -49,
        58,
        -34,
        20,
    ]
)
