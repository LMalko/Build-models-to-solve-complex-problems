import re
# 01. Add space between every dot and letter.

regex = re.compile(r"(\.)([A-Za-z])")
string = regex.sub(r"\1 \2", "stringu.numberu.booleanu.type")
print(string)

# 02. Delete 2 or more spaces.

regex = re.compile(r" {2,}")
print(regex.sub(" ", "This    is   a   waste   of    space."))

# 03. Reverse word order.

print(' '.join(reversed("words these reverse should it Now".split())))

#04. Get positions of matching sequence.

result = []
regex = re.compile(r"[a-zA-Z]{1,} [a-zA-Z]{1,} ")
for m in regex.finditer("words these reverse should it Now"):
    result.append([m.start(), m.end()])
print(result)

#5. Regex groups.

url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
match = url_regex.search("https://www.my-website.com/bio?data=blah&dog=yes")
print(f"Protocol: {match.group(1)}")
print(f"Domain: {match.group(2)}")
print(f"Everything Else: {match.group(3)}")
print(match.groups())
print(match.group())

# 6. Regex to validate users, allowed 4-16 alphanumeric and underscore.

def validate_usr(un):
    return re.match('^[a-z0-9_]{4,16}$', un) is not None

# 7. Check for alternate numbers.

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

# 8. Assign names to regex groups.

def parse_name(input):
    name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
    matches = name_regex.search(input)
    print(bool(matches))
    print(matches.group())
    print(matches.group('first'))
    print(matches.group('last'))

parse_name("Mrs. Grazyna Wojcik")

# 9. Check for correct date.

def parse_date(string):
    regex = re.compile(r"^(?P<d>[0-9]{2})[.,/](?P<m>[0-9]{2})[.,/](?P<y>[0-9]{4})$")
    matches = regex.search(string)
    if not matches:
        return None
    return {"d": matches.group("d"), "m": matches.group("m"), "y": matches.group("y")}

print(parse_date("12,04,2018"))
print(parse_date("12.05.2020"))
print(parse_date("122-077-7777"))

    #or

def parse_date(input):
    pattern = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
    match = pattern.search(input)
    if match:
        return {
            "d": match.group(1),
            "m": match.group(2),
            "y": match.group(3),
        }
    return None

# 10. Ignorecase and substitute group.

text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)

result = pattern.sub("\g<1> \g<2>", text)
print(result)
