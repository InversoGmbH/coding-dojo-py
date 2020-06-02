# Römische Zahlen umwandeln

Aufgabe ist es einen Konverter für römische Zahlen zu entwickeln. In der Datei `romanconvert.py` muss die Methode 
`roman2decimal` erweitert werden.

Diese Aufgabe wird testgetrieben umgesetzt. Für jeden Teilschritt findest du einen PyUnit-Test unter 
`/test/romanconvertkata/test_romanconvert.py`.

## Ablauf
1. Hole dir mit `git pull` die aktuelle Version des Katas.
1. Führe die Unittests aus und zeige, dass mindestens einer <span style="color:red">rot</span> ist. 
2. Arbeite dich durch die fehlgeschlagenen Testfälle durch und erweitere das Programm (nur) soweit, dass die Tests 
<span style="color:green">grün</span> werden.
3. Führe die Tests erneut durch und zeige, dass sie grün sind.
4. Führe, falls gewünscht, ein Refactoring durch.
5. Führe ein `git commit` und ein `git push` aus, um deine Änderungen allen Kata-Teilnehmern zur Verfügung zu stellen.

## Römische Zahlen
### Werte
Römische Zahl | Dezimalwert
------------- | -----------
i | 1
v | 5
x | 10
l | 50
c | 100
d | 500
m | 1000
ↁ | 5000
ↂ | 10000

### Subtraktionsregel
Die Subtraktionsregel ist eine übliche, verkürzende Schreibweise, mit der es vermieden werden soll, vier gleiche 
Zahlzeichen in direkter Aufeinanderfolge zu schreiben.

Die Subtraktionsregel in ihrer Normalform besagt, dass die Zahlzeichen I, X und C einem ihrer beiden jeweils 
nächstgrößeren Zahlzeichen vorangestellt werden dürfen und dann in ihrem Zahlwert von dessen Wert abzuziehen sind:

    I vor V oder X: IV (4), IX (9)
    X vor L oder C: XL (40), XC (90)
    C vor D oder M: CD (400), CM (900)
(Quelle [Wikipedia](https://de.wikipedia.org/wiki/R%C3%B6mische_Zahlschrift))
### Weiterführende Links
* [Wikipedia-Artikel zur Römischen Zahlschrift](https://de.wikipedia.org/wiki/R%C3%B6mische_Zahlschrift)
* [Coding-Dojo-Artikel (english)](https://codingdojo.org/kata/RomanNumerals/)