from string import ascii_lowercase , ascii_uppercase

def rot13(message):
    return message.translate(str.maketrans(ascii_lowercase + ascii_uppercase,
                                                  "".join(ascii_lowercase[13:] +
                                                  ascii_lowercase[:13] +
                                                  ascii_uppercase [13:] +
                                                  ascii_uppercase [:13])))


string = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
print(rot13(rot13(string)))
print(rot13(string))
