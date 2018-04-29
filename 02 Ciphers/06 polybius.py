from string import ascii_lowercase
from random import shuffle
import itertools
import sys
sys.path.append("..")
from resources.prettytable.prettytable import PrettyTable

# Place any key, key_a needs 5 elements, key 6 needs 6 elements.
key_y = "ABCDE"
key_x = "ABCDEF"

alphabet_order = list(ascii_lowercase)

# Shuffle elements to give extra security
shuffle(alphabet_order)

# Create table
polybius_table = PrettyTable()


# Assign elements, last row will have empty values due to alphabet only having 26 elements.
polybius_table.field_names = ["X"] + [x for x in key_y]
polybius_table.add_row([key_x[0]] + alphabet_order[0:5])
polybius_table.add_row([key_x[1]] + alphabet_order[5:10])
polybius_table.add_row([key_x[2]] + alphabet_order[10:15])
polybius_table.add_row([key_x[3]] + alphabet_order[15:20])
polybius_table.add_row([key_x[4]] + alphabet_order[20:25])
polybius_table.add_row([key_x[5]] + alphabet_order[25:] + [" ", " ", " ", " "])

print(polybius_table)


# Assign element to code.
letter_to_code = {}
for i in zip ( alphabet_order, list ( sorted ( itertools.product ( key_y, key_x ), key=lambda x: x[1] ) ) ):
    letter_to_code[i[0]] = i[1][0] + i[1][1]

def polybius_encode(message, letter_to_code):
    return "".join(letter_to_code[letter] if letter in letter_to_code.keys() else letter for letter in message.lower())

def polybius_decode(encrypted, letter_to_code):
    code_to_letter = {value: key for key, value in letter_to_code.items()}
    return " ".join(code_to_letter[code] if code in code_to_letter.keys() else code for code in encrypted.split(" "))

print(polybius_encode("d e f e n d  t h e  e a s t  w a l l  o f  t h e  c a s t l e", letter_to_code))

print(polybius_decode(polybius_encode("d e f e n d  t h e  e a s t  w a l l  o f  t h e  c a s t l e", letter_to_code),
                      letter_to_code))


# Classic version, where 'i' and 'j' share the same code.


#      1	2	3	4	  5
# 1	A	B	C	D	  E
# 2	F	G	H	I/J	  K
# 3	L	M	N	O	  P
# 4	Q	R	S	T	  U
# 5	V	W	X	Y	  Z


def polybius_encode_classic(text):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZJ'
    return ''.join(['24' if letter == 'J' else
                    str(int(alphabet.index(letter)/5 + 1)) +
                    str(int(alphabet.index(letter)%5 + 1)) if letter in alphabet else
                    letter for letter in text])

print(polybius_encode_classic("POLYBIUS SQUARE CIPHER"))