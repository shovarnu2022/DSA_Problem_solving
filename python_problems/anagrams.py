"""
Find index of anagrams?
1. create a dictionary
2. if sorted word not in dictionary,
   set word as key and index as value
3. if sorted word in dictionary,
   append index for word
"""


def anagram(arr):
    if arr is None:
        return
    else:
        dict = {}
        for i in range(len(arr)):
            word = ''.join(sorted(arr[i]))
            if word not in dict:
                dict[word] = [i+1]
            else:
                dict[word].append(i + 1)
        return dict


A = ["cat", "dog", "tca", "act"]
print(anagram(A))
