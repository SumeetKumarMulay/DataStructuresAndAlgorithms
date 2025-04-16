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
from Recursion.fib_and_memoization import fib_memo, fib_tabulation
# from Recursion.reverse import reverse
# from Recursion.isPalindrome import isPalindrome
# from Recursion.flatten import flatten
# from Recursion.capitalizeFirst import capitalizeFirst
# from Recursion.nestedEvenSum import nestedEven
# from Recursion.capitalizeWords import capitalizeWords
# from Recursion.stringifyNumber import stringifyNumbers
# from Recursion.collectStrings import collectStrings
from Recursion.fib_and_memoization import fib_generator

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
# from Sorting_Algorithms.radix_sort import radix_sort

# from Data_structures.binarysearchtree import BinarySearchTree
# from Data_structures.maxbinaryheap import MaxBinaryHeap
# from Data_structures.priorityqueue_or_minbinaryheap import PriorityQueue

# from Data_structures.weighted_graphs_and_dijkstras_algo import WeightedGraphs


# random_list = generate_random_num_list(length=1000)


# def insert_rand_values():
#     """This function add random values to the binary search tree"""
#     for x in random_list:
#         bst.insert(x)
# bst.insert_rec(10)
# bst.insert_rec(6)
# bst.insert_rec(3)
# bst.insert_rec(8)
# bst.insert_rec(15)
# bst.insert_rec(20)
# print(f"\nRandom List:: {random_list}")

# print(f"\nSize of list:: {len(random_list)}")


start = timer()

result = fib_tabulation(10000)
end = timer()

# print(f"\nResult:: {result}\n\nThe function took: {
#       round((end - start) * 1000, 5)} ms to complete!\n")
test = {
    "1": "test",
    "2": "test",
    "3": "test",
}

test1 = {
    "4": "test",
    "5": "test",
    "6": "test"
}

test3 = test | test1

l1 = ["1", "2", "3"]

# for i in range(0, len(l1)):
#     print(i)

def reverse(value: str):
    count = len(value)
    reverse_str = ""
    while count > 0:
        count = count - 1
        reverse_str = reverse_str + value[count]
    return reverse_str

x = lambda a : a[:: -1]


gen = fib_generator(1)


print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
