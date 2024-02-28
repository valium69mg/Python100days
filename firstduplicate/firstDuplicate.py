list_of_numbers = [1,2,3,4,2,6,7,9,10]
list_of_unrepeated_numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
seen_list = []

"""
IF THE LIST HAS DUPLICATES IT RETURNS TRUE 
IT TAKES TWO ARGS: arr (THE LIST TO CHECK FOR DUPLICATES) AND seen_arr (AN EMPTY INITIALIZED LIST)
"""
def first_duplicate(arr: list,seen_arr:list):
    if (arr != []):
        current_element = arr.pop()
        if (current_element in seen_list):
            return True
        seen_arr.append(current_element)

        return first_duplicate(arr,seen_arr)
    else:
        return False

print(first_duplicate(list_of_unrepeated_numbers,seen_list))


    