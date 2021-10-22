import math


def find_number(start, finish, oszthato, nem_oszthato):
    results = []
    for x in range(start, finish):
        if (x % oszthato == 0 and x % nem_oszthato != 0):
            results.append(x)
    return results


print(find_number(start=2000, finish=3201, oszthato=7, nem_oszthato=5))


def count_name(y):
    return y.count('Pista')


print(
    count_name([
        'Pista', 'Gabor', 'Pista', 'Gábor', 'István', 'István', 'László',
        'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista'
    ]))


def convert_to_number(text):
    return int(text)


def print_hello():
    x = input('input: ')
    b = convert_to_number(x)
    for i, y in enumerate(range(b)):
        print(f"{i+1}. Helló!")


print_hello()


def calculate1():
    a = input('input: ')
    r = convert_to_number(a)
    return math.pi * (r * r)


def calculate2():
    c = input('input: ')
    r = convert_to_number(c)
    return 2 * math.pi * r


print(calculate1())
print(calculate2())

names = [
    'Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter',
    'Gaál András', 'Németh Diána', 'Telek Éva', 'Ledán-Munteán Szabolcs',
    'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás'
]


def sort_and_split(list):
    x = sorted(list)
    half = round(len(x) / 2)
    first = '\n'.join(x[:half])
    second = '\n'.join(x[half:])
    nl = '\n'
    print(f" 1.csoport:{nl}{first}{nl} 2.csoport:{nl}{second}")


sort_and_split(names)
