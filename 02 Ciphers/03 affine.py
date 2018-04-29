import re
import itertools
from string import ascii_lowercase
import sys
sys.path.append("..")
from resources.words import WORDS

def affine(message, slope_a, intercept_b, decrypt=False):
    letters_to_numbers = {**{}.fromkeys(ascii_lowercase, "EMPTY"),
                          **dict(zip(ascii_lowercase,list(range(26))))}
    numbers_to_letters = {**{}.fromkeys(list(range(26)), "EMPTY"),
                          **dict(zip(list(range(26)), ascii_lowercase))}
    allowed_factors_for_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    letters = re.compile("[a-zA-Z]")
    def encipher(letter):
        return numbers_to_letters[(slope_a * letters_to_numbers[letter] + intercept_b) % 26]
    def decipher(letter):

        # Find a^-1 (the multiplicative inverse / Euclidean algorythm)
        for i in allowed_factors_for_a:
            temp = (i * slope_a) % 26
            if temp == 1:
                multiplicative_inverse_of_a = i
        return numbers_to_letters[(multiplicative_inverse_of_a
                                       * (letters_to_numbers[letter] - intercept_b)) % 26]

    if slope_a % 26 not in allowed_factors_for_a:
        return "This key a is not allowed."
    if decrypt:
        return "".join(list(map(lambda x: decipher(x) if letters.match(x) else x, message.lower())))
    return "".join(list(map(lambda x: encipher(x) if letters.match(x) else x, message.lower())))


string = "This message should be displayed from the second print 68."

test_a = 19
test_b = 25

encrypted = affine(string,test_a, test_b)
print(encrypted)
print(affine(encrypted, test_a, test_b, True))


def break_affine(message):
    hits_record = []
    allowed_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    allowed_b = list(range(26))
    allowed_a_and_b = list(itertools.product(allowed_a, allowed_b))
    for i in allowed_a_and_b:
        a = i[0]
        b = i[1]
        temp_decrypt = affine(message.lower(), a, b, True)
        hits = sum(word in WORDS for word in temp_decrypt.split())
        hits_record.append(hits)
    a_and_b = allowed_a_and_b[hits_record.index(max(hits_record))]
    return affine(message, a_and_b[0], a_and_b[1], True)



print(break_affine("icjb lhbbfvh bczpea mh ajbgefrha ouzl ich icjua gujsi 68."))