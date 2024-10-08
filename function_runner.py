"""
This is just a runner which is used to make the results look nice in the terminal as well
save on navigation time.

"""
from timeit import default_timer as timer
# # Data
from test_data.test_data import (
    generate_random_num_list,
    nested_obj,
    array_val_combo,
    longList)

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
# from Searching_Algorithams.naive_string_search import naive_string_search_v2

# # sorting algo
# from Sorting_Algorithams.bubble_sort import bubble_sort_v_1, bubble_sort_v_1_1, bubble_sort_v_2
# from Sorting_Algorithams.selection_sort import selection_sort
# from Sorting_Algorithams.insertion_sort import insertion_sort
# from Sorting_Algorithams.merge_sort import merge_sort
# from Sorting_Algorithams.quick_sort import quick_sort
from Sorting_Algorithams.radix_sort import radix_sort



random_list = generate_random_num_list(lenght=6)
print(f"\nRandom List:: {random_list}")

print(f"\nSize of list:: {len(random_list)}")

start = timer()
# NOTE insert function here.
result = radix_sort(values=random_list)
end = timer()

print(f"\nResult:: {result}\n\nThe function took: {
      round((end - start) * 1000, 5)} ms to complete!\n")
