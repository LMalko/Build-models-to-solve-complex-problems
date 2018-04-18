# 01. Exchange chars in string.

print("aei23ou".translate(str.maketrans("aeiou", "uoiea")))

# 02. Filter elements to list under condition.

    # Filter only positive numbers NOT REPEATING:
lista = [-3, -4, -1, 2, -7, 4]
print(list(filter(lambda x: x > 0, lista)))