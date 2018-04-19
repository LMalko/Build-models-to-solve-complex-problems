from string import ascii_lowercase , ascii_uppercase

def atbash(message):
    return message.translate(str.maketrans(ascii_lowercase + ascii_uppercase,
                                                  "".join(ascii_lowercase[::-1] +
                                                  ascii_uppercase [::-1])))


string = "Qzmfha Plidrm-Nrppv"
print(atbash(atbash(string)))
print(atbash(string))
