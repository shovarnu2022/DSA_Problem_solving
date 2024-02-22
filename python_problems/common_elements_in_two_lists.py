"""
l1 = [40, 50, 60, 80]
l2 = [50, 100, 150, 200]
l3 = [50]
"""


def common_elements(l1: list[int], l2: list[int]) -> None:
    common: list = []
    count: int = 0
    for num_l1 in l1:
        for num_l2 in l2:
            if num_l1 == num_l2:
                common.append(num_l1)
                count += 1

    print("Common elements in both list is : ", count)
    print(common)


def common_elements_dict(l1: list[int], l2: list[int]) -> None:
    dict1: dict = {}
    for element in l2:
        dict1[element] = 1
    count = 0
    for i in l1:
        if dict1.get(i) is not None:
            print(i)
            count += 1
    print("Number of elements common are: ", count)


list1 = [2, 4, 6, 8, 10, 12]
list2 = [3, 6, 9, 12, 15, 14]
# print(common_elements(list1, list2))
print(common_elements_dict(list1, list2))




