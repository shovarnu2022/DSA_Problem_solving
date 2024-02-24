"""
must start with vowels
abrab -> 7
"""


def amazing_substr(str1):
    vowels = "aeiouAEIOU"
    count = 0
    for i, char in enumerate(str1):
        if char in vowels:
            count += len(str1)-i
    return count


print(amazing_substr("abrab"))
