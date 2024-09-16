from test_data.test_array import nested_obj

from Recursion.basic_count_down import countDown
from Recursion.sum_range import sum_range
from Recursion.factorial import factorial
from Recursion.power import power
from Recursion.product_array import product_array
from Recursion.recursive_range import recursive_range
from Recursion.fib import fib
from Recursion.reverse import reverse
from Recursion.isPalendrome import isPalendrone
from Recursion.flatten import flatten
from Recursion.capitalizeFirst import capitalizeFirst
from Recursion.nestedEvenSum import nestedEven
from Recursion.capitalizeWords import capitalizeWords
from Recursion.stringifyNumber import stringifyNumbers
from Recursion.collectStrings import collectStrings
from Searching_Algorithams.linear_search import LinearSearch


def function_runner(func):
    result = func
    print(f"result:: {result}")


function_runner(LinearSearch(array=["Sumito", "JOHN", "RON"], values="JOHN"))
