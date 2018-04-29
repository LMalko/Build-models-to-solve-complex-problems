from itertools import cycle, islice, chain
import re

def rail_fence(message, key):

    non_alpha_numeric = re.compile(r"[^a-zA-Z0-9]")
    message = re.sub(non_alpha_numeric, "", message).lower()

    container_forward = [i for i in range(key)]
    container_back = reversed(container_forward[1: -1])
    container = cycle(chain(container_forward, container_back))

    container_slice = list(islice(container, len(message)))

    letters_enumerate = zip(list(message), container_slice)

    result = sorted(letters_enumerate, key=lambda x: x[1])

    return "".join(x[0] for x in result)


print(rail_fence("It is a transposition cipher that follows a simple rule for mixing up "
                 "the characters in the plaintext to form the ciphertext.", 5))


def rail_fence_decode(message, key):

    non_alpha_numeric = re.compile(r"[^a-zA-Z0-9]")
    message = re.sub(non_alpha_numeric, "", message).lower()

    container_forward = [i for i in range(key)]
    container_back = reversed(container_forward[1: -1])
    container = cycle(chain(container_forward, container_back))
    container_slice = list(islice(container, len(message)))

    row = 0
    list_start= 0

    for i in message:

        if row in container_slice[list_start:]:
            container_slice[container_slice.index(row)] = i
            list_start += 1
        else:
            list_start = 0
            row += 1
            container_slice[container_slice.index(row)] = i

    return "".join(container_slice)


print(rail_fence_decode(rail_fence("It is a transposition cipher that follows a simple rule for mixing up "
                 "the characters in the plaintext to form the ciphertext.", 700), 700))