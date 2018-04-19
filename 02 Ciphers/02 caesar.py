from string import ascii_lowercase , ascii_uppercase
import random

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


