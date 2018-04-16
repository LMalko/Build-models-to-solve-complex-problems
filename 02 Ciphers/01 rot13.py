

def rot13(in_string):
    decoded = ""
    for char in in_string:
        if "a" <= char <= "z":
            decoded += chr(ord("a") + (ord(char) - ord("a") + 13) % 26)
        elif "A" <= char <= "Z":
            decoded += chr(ord("A") + (ord(char) - ord("A") + 13) % 26)
        else:
            decoded += char
    return decoded


string = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
print(rot13(rot13(string)))
print(rot13(string))
