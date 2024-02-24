"""
Given a string. Extract all the numbers in the string and return
the numbers as a list.

Input:  str = "I am 89 years old My father name is 120"

Output: [89, 120]
"""

import re
sentence = "Nancy is 90 years old. She wants 120.6 toffees"
# num = []
# for word in sentence.split():
#     if not word.isalpha():
#         num.append(word)
#
# print(num)

# digit = re.findall('\d*\.?\d+', sentence)
digit = re.findall('\d*\.+\d+', sentence)
print(digit)




