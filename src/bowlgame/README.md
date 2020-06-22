# BowlGame
## Aufgabe
Für ein Spiel (`game`), in dem ein Spieler mit einer Kugel (`bowl`) Kegel ( `pin`, Anzahl = `p`) umwirft, sollen für
einen Spieler die Punkte gezählt werden. Dafür wird (im Test) eine Instanz einer Klasse erzeugt. 
Jedes Spiel besteht aus `n` Durchgänge (`frame`). 
In jedem Durchgang hat der Spieler `s` Würfe, mit denen er die Kegel abräumen kann. 
Ein umgeworfener Kegel ist ein Punkt.
  
Das Spiel besitzt eine Methode `get_score()->int`, mit der ich mir stets die bereits erspielte Gesamtpunktzahl anzeigen
lassen kann.

Außerdem existiert eine Methode `is_frame()->int`, mit der ich mir stets zurück geben kann, welcher Frame gerade
gespielt wird. Mit der Methode `get_frame()->Frame` kann ich mir den aktuellen Frame zurück geben lassen. Ist der Frame
bereits beendet, muss ein neuer Frame erzeugt und zurückgegeben werden. 

Der Frame hat eine Methode `shot(pin_count:int)` mit der die Anzahl der umgeworfenen Pins für einen Wurf übergeben 
werden kann.

Folgende Exceptions stehen im Modul `bowlexception` zur Verfügung:
* `BowlToManyShots`: Fehler, der geworfen wird, wenn in einem Frame mehr Würfe gemacht werden, als erlaubt
* `BowlToManyPins`: Fehler, der geworfen wird, wenn zuviele Pins umgeworfen wurden
* `BowlGameEnds`: Fehler, der geworfen wird, wenn das Spiel beendet wurde und ein neuer Frame angefordert wird 
(`get_frame()->Frame`)


> Mir ist bewusst, dass die Regeln in der Realität deutlich komplexer ausfallen.
> Um das Kata im zeitlichen Rahmen zu halten, wurde die Aufgabe vereinfacht.

## Bowling

Ein Spiel hat 10 Durchgänge (`n`). 
Es stehen 10 Kegel auf dem Feld (`p`). 
Der Frame besteht stets aus zwei Würfen (`s`).
Beim zweiten Wurf, werden die umgeworfenen Kegel des ersten Wurfs nicht wieder aufgestellt. Wurden beim ersten Wurf
alle Kegel umgeworfen, entfällt der zweite Wurf.

Siehe auch [Wikipedia:Bowling](https://de.wikipedia.org/wiki/Bowling)

## Kegeln 
Auf der Bahn stehen 9 Kegel (`p`). 
Ein Spiel hat soviele Durchgänge (`n`), bis die Punktzahl 25 erreicht oder überschritten wurde (`score >= 25`).

Solange in einem Durchgang bei einem Wurf nur drei, zwei oder ein Kegel abgeräumt wurden, darf erneut geworfen werden.
Es zählen nur Würfe mit drei, zwei oder einem Punkt. _Nach jedem Wurf werden wieder alle Kegel aufgestellt._

Das heißt, wirft jemand keine Kegel oder mehr als vier Kegel, zählt der Wurf nicht und der nächste Frame ist dran.

Beispielrechnung: Ein Spieler wirf in einem Frame 3, 3, 2, 7 Kegel um, dann ist der Frame beendet und er hat 3+3+2=8 
Punkte. 

Siehe auch [Wikipedia:Kegeln](https://de.wikipedia.org/wiki/Kegeln)
Angelehnt an [Drei&weniger](https://www.planet-wissen.de/gesellschaft/sport/kegeln/pwiekegelspiele100.html)
