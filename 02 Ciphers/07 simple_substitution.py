from string import ascii_lowercase
from random import shuffle

def simple_substitution(message, key, decrypt=False):
    if not decrypt:
        return message.lower().translate(str.maketrans(ascii_lowercase, key))
    return message.lower().translate(str.maketrans(key, ascii_lowercase))


temp_key = list(ascii_lowercase)
shuffle(temp_key)
temp_key = "".join(temp_key)
print(f"Temp key: {temp_key}")
message = "Composition is achieved by using instance variables that refers to other objects."

print(simple_substitution(message, temp_key))
print(simple_substitution("rmfqmghzhms hg erkhpypi ux nghsw hsgzesrp yelheucpg zkez " +
                          "lpbplg zm mzkpl muvprzg.", "euripbwkhvtcfsmqdlgznyojxa", True))




# Shorter version will return inaccurate results, longer version will take days and it's not tested
# It's faster to break it manually.

import re
import itertools
from words import WORDS
from collections import Counter

# Shorter version using relative occurence of letters in English language.

# def break_simple_substitution(message):
#     message = message.lower()
#
#     regex = re.compile(r"[^a-z]")
#
#     letters_occurence = Counter(re.sub(regex, "", message))
#
#     letters_freq_sorted = "".join (sorted (letters_occurence.keys(),
#                                                        key=lambda x: letters_occurence[x], reverse=True))
#
#     most_frequent_letters = ["e", "a", "i", "t", "o", "n", "s", "h", "r", "d", "l", "c"]
#     hits_list = []
#
#
#     for i in itertools.permutations(most_frequent_letters):
#         temp_decrypt = message.translate(str.maketrans(letters_freq_sorted[:12], "".join(i)))
#         hits = sum(word in WORDS for word in temp_decrypt.split())
#         hits_list.append(hits)
#         if hits > 3:
#             print(temp_decrypt, max(hits_list), i)
#             break
#         print(len(hits_list))





# Brute force verion.

# def break_simple_substitution(message):
#     # Make sure there are all the letters.
#     message = message.lower() + ascii_lowercase
#
#     for i in itertools.permutations(ascii_lowercase):
#         temp_decrypt = message.translate(str.maketrans(ascii_lowercase, "".join(i)))
#         hits = sum(word in WORDS for word in temp_decrypt.split())
#         if hits > 4:
#             return temp_decrypt[:-26]




