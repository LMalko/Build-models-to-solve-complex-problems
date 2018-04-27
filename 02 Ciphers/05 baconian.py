from string import ascii_lowercase

def baconian(message, key, decipher=False):
    if not decipher:
        return " ".join([key[ascii_lowercase.index(letter)] if letter in ascii_lowercase else letter for letter in message.lower()])
    return "".join([ascii_lowercase[key.index(sequence)] if sequence in key else sequence for sequence in message.split(" ")])

unique_code_version = ['aaaaa', 'aaaab', 'aaaba', 'aaabb', 'aabaa', 'aabab', 'aabba', 'aabbb',
                       'abaaa', 'abaab', 'ababa', 'ababb', 'abbaa', 'abbab', 'abbba', 'abbbb', 'baaaa',
                       'baaab', 'baaba', 'baabb', 'babaa', 'babab', 'babba', 'babbb', 'bbaaa', 'bbaab']

standard_version = ['aaaaa', 'aaaab', 'aaaba', 'aaabb', 'aabaa', 'aabab', 'aabba', 'aabbb',
                       'abaaa', 'abaaa', 'abaab', 'ababa', 'ababb', 'abbaa', 'abbab', 'abbba', 'abbbb', 'baaaa',
                       'baaab', 'baaba', 'baabb', 'baabb', 'babaa', 'babab', 'babba', 'babbb']

print(baconian("STRIKENOW!",
               standard_version))

print(baconian("STRIKENOW!",
               unique_code_version))

print(baconian("baaab baaba baaaa abaaa abaab aabaa abbaa abbab babaa !",
               standard_version, decipher=True))

print(baconian("baaba baabb baaab abaaa ababa aabaa abbab abbba babba !",
               unique_code_version, decipher=True))

