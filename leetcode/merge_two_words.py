"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating 
order, starting with word1. If a string is longer than the other, append the additional letters 
onto the end of the merged string.
"""


def merge_two_words(word1: str, word2: str) -> str:

    pointer_1 = 0
    pointer_2 = 0

    new_str = ""

    while pointer_1 < len(word1) or pointer_2 < len(word2):
        if pointer_1 < len(word1) or pointer_2 > len(word2):
            new_str = f"{new_str}{word1[pointer_1]}"
            pointer_1 += 1
        if pointer_2 < len(word2) or pointer_1 > len(word1):
            new_str = f"{new_str}{word2[pointer_2]}"
            pointer_2 += 1
    return new_str
