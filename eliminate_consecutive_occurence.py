def eliminate_consecutive(input_list):
    result = []
    i = 0
    while i < len(input_list):
        # Check if the current element is not equal to the next element and the previous element is not equal to the current element
        if (i == 0 or input_list[i] != input_list[i - 1]) and (
                i == len(input_list) - 1 or input_list[i] != input_list[i + 1]):
            result.append(input_list[i])
        elif i < len(input_list) - 1 and input_list[i] == input_list[i + 1]:
            # Skip the consecutive duplicates
            i += 1
        i += 1

    return result


# Example usage:
list1 = [1, 2, 2, 3, 4, 5, 5, 3]
output_result = eliminate_consecutive(list1)
print(output_result)
