# 01. Exchange chars in string.

print("aei23ou".translate(str.maketrans("aeiou", "uoiea")))

# 02. Filter elements to list under condition.

    # Filter only positive numbers NOT REPEATING:
lista = [-3, -4, -1, 2, -7, 4]
print(list(filter(lambda x: x > 0, lista)))

# 03. Sort under condition without changing elements.

lista = ["a", "C", "b", "a", "c", "A"]
print(sorted(lista, key=lambda x: x.lower(), reverse=True))
    # min(lista, key=lambda number: number * number)
    # max(lista, key=lambda number: number * number)

# 04. Keeping track how many times a function was called.

def running_average():
    running_average.counter = 0
    running_average.total = 0
    def funkcja(number):
        running_average.counter += 1
        running_average.total += number
        return running_average.total / running_average.counter
    return funkcja

    # rAvg = running_average();
    # rAvg(10) // 10.0;
    # rAvg(11) // 10.5;
    # rAvg(12) // 11;
    #
    # rAvg2 = running_average()
    # rAvg2(1) // 1
    # rAvg2(3) // 2