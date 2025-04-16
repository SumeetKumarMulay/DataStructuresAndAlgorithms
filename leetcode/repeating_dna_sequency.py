"""LINK:
{https://leetcode.com/problems/repeated-dna-sequences/?envType=problem-list-v2&envId=string}
"""

from typing import List


def find_repeated_dna_sequences(s: str) -> List[str]:
    """t"""
    counter = {}
    final_list = []

    for i in range(len(s) - 9):
        s_str = s[i:i+10]
        if s_str in counter:
            counter[s_str] += 1
        else:
            counter[s_str] = 1
    for key in counter:
        value = counter.get(key)
        if value > 1:
            final_list.append(key)
    return final_list


res = find_repeated_dna_sequences(s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")

print(res)
