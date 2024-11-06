def find_duplicates(input_list):
    seen = set()
    duplicates = set()
    
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)


my_list = [1, 2, 3, 4, 2, 5, 3, 6, 1]
duplicates = find_duplicates(my_list)
print("Duplicates:", duplicates)