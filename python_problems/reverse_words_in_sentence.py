"""
Udemy is an online platform
reverse: platform online is an Udemy
"""


def reverse(str_r):
    str_r = str_r[::-1]
    return str_r


def reverse_words(str_r):
    n = len(str_r)
    if n == 1:
        return str_r
    str2 = str_r.split(" ")
    size = len(str2)
    rev_all = ""
    for i in range(0, size):
        rev = reverse(str2[i])
        rev_all = rev_all + rev + " "
    d = reverse(rev_all)
    return d.strip()


msg = "Udemy is an online platform"
print(reverse_words(msg))
