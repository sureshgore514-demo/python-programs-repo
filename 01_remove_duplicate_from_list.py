'''
Docstring for 01_remove_duplicate_from_list

This script defines a function to remove duplicate elements from a list while preserving the original order of elements.

'''

def remove_duplicates(input_list):
    output_list = []
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    return output_list


list1 = [1,2,8,2,3,4,4,5,5,5,6,7,7,8,9]
result = remove_duplicates(list1)
print(result)  # Output: [1, 2, 8, 3, 4, 5, 6, 7, 9]