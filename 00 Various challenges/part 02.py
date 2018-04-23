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

# 05. Allowing function be called only once.

def once(funkcja):
    once.count = 0
    def funkcja(a, b):
        once.count += 1
        if once.count > 1:
            return None
        return a + b
    return funkcja

def add(a,b):
    return a+b

oneAddition = once(add)

print(oneAddition(2,2))
print(oneAddition(2,2))
print(oneAddition(12,200))

import re
# 06. Add space between every dot and letter.

regex = re.compile(r"(\.)([A-Za-z])")
string = regex.sub(r"\1 \2", "stringu.numberu.booleanu.type")
print(string)

# 07. Delete 2 or more spaces.

regex = re.compile(r" {2,}")
print(regex.sub(" ", "This    is   a   waste   of    space."))

# 08. Reverse word order.

print(' '.join(reversed("words these reverse should it Now".split())))

#09. Get positions of matching sequence.

result = []
regex = re.compile(r"[a-zA-Z]{1,} [a-zA-Z]{1,} ")
for m in regex.finditer("words these reverse should it Now"):
    result.append([m.start(), m.end()])
print(result)

# 10. Regex to validate users, allowed 4-16 alphanumeric and underscore.

def validate_usr(un):
    return re.match('^[a-z0-9_]{4,16}$', un) is not None

# 10.5. Check for alternate numbers.

postalCode= "323232"

# Compile once to use later.
regexu = re.compile(r"^[1-9][0-9]{5}$")
# Search for only first match.
result = regexu.search(postalCode).group()
print(result)
# Find all non overlapping matches.
result = regexu.findall(postalCode)
print(result)
alternatingDigitPairs= re.search(r'(\d)(\d)\1\2', postalCode).group()
print(alternatingDigitPairs)
