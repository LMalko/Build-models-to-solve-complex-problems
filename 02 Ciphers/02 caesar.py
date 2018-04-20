from string import ascii_lowercase , ascii_uppercase
import random
from words import WORDS

def caesar(message, offset, decrypt=False):
    if decrypt:
        offset = 0 - offset
    offset = offset % 26 if offset > 26  or offset < -26 else offset
    return message.translate(str.maketrans(ascii_lowercase + ascii_uppercase,
                                                  "".join(ascii_lowercase[offset:] +
                                                  ascii_lowercase[:offset] +
                                                  ascii_uppercase [offset:] +
                                                  ascii_uppercase [:offset])))

string = "This message should be displayed from the second print."

test_offset = random.randrange(-300, 300)

caesar_encrypt = caesar(string, test_offset)
print(caesar_encrypt)
caesar_decrypt = caesar(caesar_encrypt, test_offset, True)
print(caesar_decrypt)



def break_caesar(message):
    caesar_lambda = lambda s, key: s.translate(str.maketrans(ascii_lowercase, ascii_lowercase[key:] + ascii_lowercase[:key]))

    message_only_alpha = ''.join(c if c.isalpha() else ' ' for c in message).lower()

    hits = [ sum(w in WORDS for w in caesar_lambda(message_only_alpha, -key).split()) for key in range(26) ]

    most_likely_offset = hits.index(max(hits))

    return caesar(message, most_likely_offset, True)

print(break_caesar("Gur dhvpx oebja sbk whzcf bire gur ynml qbt."))



