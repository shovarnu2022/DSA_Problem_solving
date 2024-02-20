"""
NETSET -> ETSETN -> TSETNE -> SETNET

Algorithm :

1. Concatenate string with itself
2. Traverse the concatenated string from 0 to size-1
3. print all substring

size = len(str)
temp = str + str
i loop from 0 to size
  j loop from 0 to size
    print temp[i+j]
"""


def leftRotatedString(name):
    size = len(name)

    temp = name + name

    for i in range(size):
        for j in range(size):
            print(temp[i + j], end="")
        print()


string = "NETSET"
leftRotatedString(string)


def checkrotation(str1, str2):
    if len(str1) != len(str2):
        return False
    size = len(str1)
    s = str1+str1
    if str2 in s:
        print(str1, "matching with", str2)
    else:
        print(str1, "is not matching with", str2)

checkrotation("ANU", "NUA")
