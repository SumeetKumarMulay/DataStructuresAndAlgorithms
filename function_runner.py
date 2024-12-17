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
# from Recursion.isPalindrome import isPalindrome
# from Recursion.flatten import flatten
# from Recursion.capitalizeFirst import capitalizeFirst
# from Recursion.nestedEvenSum import nestedEven
# from Recursion.capitalizeWords import capitalizeWords
# from Recursion.stringifyNumber import stringifyNumbers
# from Recursion.collectStrings import collectStrings

# # Searching Functions

# from Searching_Algorithms.linear_search import LinearSearch
# from Searching_Algorithms.binary_search import BinarySearch
# from Searching_Algorithms.naive_string_search import naive_string_search_v2

# # sorting algo
# from Sorting_Algorithms.bubble_sort import bubble_sort_v_1, bubble_sort_v_1_1, bubble_sort_v_2
# from Sorting_Algorithms.selection_sort import selection_sort
# from Sorting_Algorithms.insertion_sort import insertion_sort
# from Sorting_Algorithms.merge_sort import merge_sort
# from Sorting_Algorithms.quick_sort import quick_sort
#from Sorting_Algorithms.radix_sort import radix_sort

from Data_structures.binarysearchtree import BinarySearchTree

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(17)
bst.insert(17)




# random_list = generate_random_num_list(length=6)
# print(f"\nRandom List:: {random_list}")

# print(f"\nSize of list:: {len(random_list)}")

start = timer()
# NOTE insert function here.
bst.inorder(bst.root)
result = bst.contains(2)
end = timer()

print(f"\nResult:: {result}\n\nThe function took: {
      round((end - start) * 1000, 5)} ms to complete!\n")
