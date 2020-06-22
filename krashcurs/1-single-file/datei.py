#!//usr/bin/env python3
# -*- coding: utf-8 -*-

print("Hello World")

print("Hello", "World", sep=", ")

hello_world = "Hallo"

if hello_world is not None:
    print(hello_world)
    print("Moin")

for i in range(0, 5):
    print(i)

for zeichen in hello_world:
    print(zeichen)

i = 7
while i > 0:
    print(i)
    i -= 1  # i = i-1

# Einzeiliges Kommentar

"""
Mehrzeiliges Kommentar
Bubu
"""

'''

'''


def funktion(wert: str = "default"):
    print(wert)


funktion("Hi")
funktion()
funktion(1)


def dividiere(zaehler: int, nenner: int) -> int:
    return int(zaehler / nenner)


print(dividiere(1, 1))
print(dividiere(4, 2))
print(dividiere(zaehler=2, nenner=3))

try:
    print(dividiere(1, 0))
except ZeroDivisionError as e:
    print("Division durch Null")
    # raise Exception("Division durch null ist nicht erlaubt")


class Mensch:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

    def __str__(self):
        return "Name: %s" % self.name


chef = Mensch('Boss')

print(chef)
