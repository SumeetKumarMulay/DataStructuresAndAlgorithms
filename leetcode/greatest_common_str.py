"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e.,
t is concatenated with itself one or more times). Given two strings str1 and str2, return the 
largest string x such that x divides both str1 and str2.
"""


def greatest_common_str(str1: str, str2: str,) -> str:

    is_squence = False

    def expected(str1: str, str2: str, expected_str: str = "") -> str:
        if len(expected_str) <= len(str1):
            expected_str = f"{expected_str}{str2}"
            return expected(str1=str1, str2=str2, expected_str=expected_str)
        return expected_str

    def check_seq(str1: str, str2: str) -> bool:
        nonlocal is_squence
        if len(str1) == 0:
            return is_squence
        pointer_1 = 0
        pointer_2 = len(str2)
        if str1[pointer_1: pointer_2] == str2:
            is_squence = True
            return check_seq(str1=str1[pointer_2:], str2=str2)
        is_squence = False
        return is_squence

    def checker(str1: str, str2: str) -> str:
        if len(str2) == 0:
            return str2
        
        if check_seq(str1=str1, str2=str2):
            return checker(str1=str1, str2=str2[1:])
        

    return checker(str1=str1, str2=str2)
