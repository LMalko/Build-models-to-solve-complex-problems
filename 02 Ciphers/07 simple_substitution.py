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





from collections import Counter
import re
import itertools
from words import WORDS

# 26 letter permutations cause MemoryError.
# For longer text one can substitute letters using relative frequency in the English language.


def break_simple_substitution(message):
    message = message + ascii_lowercase

    hits_list_one = []

    for i in itertools.permutations(ascii_lowercase):
        temp_decrypt = message.translate(str.maketrans(ascii_lowercase, "".join(i)))
        hits = sum(word in WORDS for word in temp_decrypt.split())
        hits_list_one.append(hits)
        print(temp_decrypt, max(hits_list_one))
        if hits > 3:
            break

    print(temp_decrypt[:-26])


break_simple_substitution("rmfqmghzhms hg erkhpypi ux nghsw hsgzesrp yelheucpg zkez " +
                          "lpbplg zm mzkpl muvprzg.")

