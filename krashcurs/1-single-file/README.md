# KrashCurs Python
## Am Anfang war eine Datei

* datei.py
  * [Shebang](https://de.wikipedia.org/wiki/Shebang):
```python
#!/usr/bin/env python3
```
  * [Encoding](https://www.python.org/dev/peps/pep-0263/): 
```python
# -*- coding: utf-8 -*-
```
  * [Namenskonvention](https://www.python.org/dev/peps/): 
    * Verzeichnis: nur Kleinbuchstaben/Zahlen
    * Datei: nur Kleinbuchstaben/Zahlen/Unterstriche, endet auf `.py`
  * einfache Befehle: Jede Zeile ein Befehl
```python
print("Ich bin da")
print("Mein Name ist", "Dojo-Master") # Trennzeichen

hallo_welt = "Hallo Welt"
print(hallo_welt)

if hallo_welt is not None:
    print(hallo_welt)

for zeichen in hallo_welt:
    print(zeichen)

i = 50
while i > 0:
    print(i)  # Schreibe i auf stdout
    i -= 1  # Dekrement um eins

# Kommentar
"""
Mehrzeiliges Kommentar
"""

'''
Mehrzeiliges Kommentar
'''

```
* Funktion selber bauen
  * Namenskonvention: nur Kleinbuchstaben/Zahlen/Unterstriche ([SnakeCase](https://en.wikipedia.org/wiki/Snake_case))
```python
def funktion(wert: str = ""):
    print("Hallo Welt")
    print(wert)
    print(type(wert))

funktion(123)

def dividiere(zaehler: int, nenner: int)-> int:
    print("%i / %i" % (zaehler, nenner))
    return zaehler / nenner

print(" = %i" % dividiere(2, 1))
print(" = %i" % dividiere(2, 2))
print(" = %i" % dividiere(0, 1))

try:
    print(" = %i" % dividiere(1, 0))
except ZeroDivisionError as e:
    print("ups...", e)

```
* Klasse selber bauen
  * Namenskonvention: Großbuchstabe am Anfang + [CamelCase](https://en.wikipedia.org/wiki/Camel_case
```python
class Mensch:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Name: %s" % self.name

class SuperMensch(Mensch):
    def print_ist_super(self):
        print("%s is super" % self.name)


chef = Mensch('Boss')

print(chef)

print(chef)

```