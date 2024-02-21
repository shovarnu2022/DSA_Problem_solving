"""
ord - Given for string. Return an integer representing the
unicode Code point of the character when the argument is a
unicode object
"""


def exceltitle_num(str_r):
    size = len(str_r)
    result = 0
    for i in range(size):
        num = ord(str_r[i])-ord('A')+1
        result = result + num*pow(26, size-1)
        size = size-1
    return result


str_r = "Y"
print(exceltitle_num(str_r))


