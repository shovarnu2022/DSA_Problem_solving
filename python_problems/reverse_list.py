list2 = []
list1 = [4, 7, 9, 2]


list2 = [list1[i] for i in range(len(list1)-1, -1, -1)]
print(list2)
