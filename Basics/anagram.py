"""
Write a function that can accepts two string and checks if they are anagrams of 
each other. 
"""


def valid_anagram(string1: str, string2: str) -> bool:
    """we check is the len of the two strings are the same and that they are not the
    same strings."""
    if len(string1) != len(string2):
        return False
    else:
        # setting up a counter
        counter1 = {}
        counter2 = {}
        # checking frequency
        for alpha in string1:
            if counter1.get(alpha):
                counter1[alpha] += counter1[alpha]
            else:
                counter1[alpha] = 1
        for alpha in string2:
            if counter2.get(alpha):
                counter2[alpha] += counter2[alpha]
            else:
                counter2[alpha] = 1
        # compairing both the strings.
        for key, value in counter1.items():
            if not key in counter2:
                return False
            if counter2[key] != counter1[key]:
                return False
        return True
