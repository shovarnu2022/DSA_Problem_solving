#amazingsubstring

#starts with vowels
#abrab -> 8


def amazing_substr(str1):
    vowels = "aeiouAEIOU"
    count = 0
    for index, char in enumerate(str1):
        if char in vowels:
            count += len(str1)-index
    return count


str1 = "abrab"
print(amazing_substr(str1))

