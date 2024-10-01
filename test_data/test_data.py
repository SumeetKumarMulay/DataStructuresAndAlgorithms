import random


nested_obj = {
    "a": 2,
    "b": {"c": 4, "d": {"e": 6, "f": 8}},
    "g": 10,
    "h": "not a number",
    "i": [12, 13, 14],
}

sort_one_to_five_list = [1, 2, 3, 4, 5]
sort_long_list = [
    5,
    6,
    10,
    13,
    14,
    18,
    30,
    34,
    35,
    37,
    40,
    44,
    64,
    79,
    84,
    86,
    95,
    96,
    98,
    99,
]

array_val_combo = {
    "1": {
        "array": sort_one_to_five_list,
        "value": 2,
    },
    "2": {
        "array": sort_one_to_five_list,
        "value": 3,
    },
    "3": {
        "array": sort_one_to_five_list,
        "value": 5,
    },
    "4": {
        "array": sort_one_to_five_list,
        "value": 6,
    },
    "6": {
        "array": sort_long_list,
        "value": 10,
    },
    "7": {
        "array": sort_long_list,
        "value": 95,
    },
    "8": {
        "array": sort_long_list,
        "value": 100,
    },
}

longList: list[int] = [
    42,
    67,
    23,
    89,
    12,
    56,
    34,
    90,
    2,
    78,
    54,
    11,
    99,
    45,
    66,
    33,
    88,
    13,
    57,
    35,
    91,
    24,
    79,
    55,
    14,
    92,
    46,
    67,
    36,
    87,
    15,
    58,
    37,
    93,
    25,
    80,
    56,
    16,
    94,
    47,
    68,
    38,
    89,
    17,
    59,
    39,
    95,
    26,
    81,
    57,
    18,
    96,
    48,
    69,
    30,
    82,
    19,
    60,
    40,
    97,
    27,
    83,
    51,
    20,
    98,
    49,
    70,
    31,
    84,
    52,
    21,
    99,
    50,
    71,
    32,
    85,
    53,
    22,
    100,
    41,
    62,
    33,
    86,
]


def generate_random_num_list(lenght: int = None,
                         max_val: int = None,
                         min_val: int = None,) -> list[int]:
    """
    Generates a random list of numbers. 

    Args:
        lenght (int, optional): Use this if you want a list of a given size. Defaults to None so, 
        a random values will be selected.
        max_val (int, optional): Use this to provide a max value. Defaults to None so, 
        a random values will be selected. 
        min_val (int, optional): Use this to provide min value. Defaults to None so, 
        a random values will be selected.

    Returns:
        list[int]: returns a random list of integers. 
    """
    random_list: list[int] = []
    mx = max_val if max_val is not None else random.randint(100, 200)
    mn = min_val if min_val is not None else random.randint(1, 99)
    size = lenght if lenght is not None else random.randint(60, 500)

    for _ in range(size):
        generate_int = random.randint(mn, mx)
        random_list.append(generate_int)
    return random_list
