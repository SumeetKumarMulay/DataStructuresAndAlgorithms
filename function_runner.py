"""
This is just a runner which is used to make the results look nice in the terminal as well 
save on navigation time.

"""

# # Data
# from test_data.test_data import nested_obj, array_val_combo

# # Recursion Functions
# from Recursion.basic_count_down import countDown
# from Recursion.sum_range import sum_range
# from Recursion.factorial import factorial
# from Recursion.power import power
# from Recursion.product_array import product_array
# from Recursion.recursive_range import recursive_range
# from Recursion.fib import fib
# from Recursion.reverse import reverse
# from Recursion.isPalendrome import isPalendrone
# from Recursion.flatten import flatten
# from Recursion.capitalizeFirst import capitalizeFirst
# from Recursion.nestedEvenSum import nestedEven
# from Recursion.capitalizeWords import capitalizeWords
# from Recursion.stringifyNumber import stringifyNumbers
# from Recursion.collectStrings import collectStrings

# # Searching Functions

# from Searching_Algorithams.linear_search import LinearSearch
# from Searching_Algorithams.binary_search import BinarySearch
from Searching_Algorithams.naive_string_search import naive_string_search_v2


def function_runner(func):
    """just a print statment"""
    result = func
    print(f"result:: {result}")


function_runner(
    naive_string_search_v2(first_str="бобагбоб фдгапк бобфмкгбоб", second_str="боб")
)
