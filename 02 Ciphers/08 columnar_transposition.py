import sys
sys.path.append("..")
from resources.prettytable.prettytable import PrettyTable
from itertools import chain


def show_phase_one(message, key):

    message = message.replace(" ", "")
    message += "x" * (len( key) - len(message) % len(key))

    table = PrettyTable()
    table.field_names = [letter for letter in key]

    rows_amount = int(len(message) / len(key))

    start = 0
    step = len(key)
    for i in range(rows_amount):
        table.add_row([letter for letter in message[start: start + step]])
        start += step
    return table

def columnar_transposition(message, key):
    message = message.replace(" ", "")
    message += "x" * (len(key) - len(message) % len(key))

    columns = []
    for i in range(len(key)):
        columns.append([key[i]] + [[message[index]
                                    for index in range(len(message))
                                    if index % len(key) == i]])

    columns.sort(key=lambda x: x[0])

    try:
        table = PrettyTable()
        table.field_names = [column[0] for column in columns]

        rows_amount = int(len(message) / len(key))

        for i in range(rows_amount):
            table.add_row([column[1][i] if i <= len(column[1]) else "x" for column in columns])

        print(table)
    except:
        print("Table unsuccessful")

    print("Encoded: \n")

    return "".join(list(chain.from_iterable([i[1] for i in columns])))

def decode_columnar_transposition(message, key):
    sorted_key = sorted(key)

    columns = []

    start = 0
    step = int(len(message) / len(key))


    for i in range(len(key)):
        columns.append([sorted_key[i]] + [letter for letter in message[start: start + step]])
        start += step


    columns.sort(key=lambda x: key.index(x[0]))

    result = ""

    rows_amount = int(len(message) / len(key))
    for i in range(rows_amount):
        result += "".join([column[i + 1] for column in columns])

    return result



print("Phase one: \n")
try:
    print(show_phase_one("The key for the columnar transposition cipher is a keyword", "PYTHONRIDE"))
except:
    print("Table unsuccessful")
print("Phase two: \n")
print(columnar_transposition("The key for the columnar transposition cipher is a keyword", "PYTHONRIDE"))
print("Decode: \n")
print(decode_columnar_transposition("rairdtrtixkonceonseryuppwelsiyThtisfmohoecankheroa", "PYTHONRIDE"))