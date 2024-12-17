"""
Write a radix sort function which takes in a list of base 10 numbers and sorts them. 
1. Write a function which takes two number, the first number is the data to be used 
in the function and second number is the position which is used the find the digit in 
the first number.
2. Write a function which takes in a number and return the number of digits in that number
3. Write a function which uses the above function and accepts a list of numbers. It should
then return the number of digits in the largest number.
"""
from math import log10


def get_digit(number: int, position: int) -> int:
    """
    This function return the digit in the position of number. 
    Eg: get_digit(number=2437, position=4) -> 7 

    Args:
        number (int): The number who's digit you want to find. 
        position (int): The position of the digit you are interested in. 

    Returns:
        int: The digit in question.
    """
    digit = int(abs(number) / pow(10, position)) % 10
    return digit


def most_digits(values: list[int]) -> int:
    """
    Accepts a list of numbers. It should then return the number of 
    digits in the largest number.
    Args:
        values (list[int]): list of number

    Returns:
        int: number of digits in the largest number.
    """

    def get_count(number: int) -> int:
        """
        This function takes in a number and return the number of digits in that number.
        Args:
            number (int): The number who's digits you want to find.

        Returns:
            int: number of digits in number.
        """
        if number == 0:
            return 1
        digit = int(log10(abs(number))) + 1
        return digit

    max_digit = max(values)
    no_digits = get_count(max_digit)

    return no_digits


def radix_sort(values: list[int]) -> list[int]:
    """
    Uses radix sort method to sort a list of unsorted values

    Args:
        values (list[int]): takes in unsorted list.

    Returns:
        list[int]: A sorted list
    """
    max_digits = most_digits(values=values)
    for k in range(0, max_digits):
        bucket = [[] for _ in range(10)]
        for i in range(len(values)):
            digit = get_digit(number=values[i], position=k)
            bucket[digit].append(values[i])
        values = [item for sublist in bucket for item in sublist]
        # values = list(itertools.chain.from_iterable(bucket))
    return values
