Hat jemand Gewonnen?
    - spalte 1, 2, 3, 4 gleiche steine hineinwerfen das es eine reihe ergibt
    - in spalte 1 4 gleiche steine hineinwerfen
    - diagonale testen mit gleichen steinen
    - testen innerhalb des feldes (nicht bei spalte 1 beginnent)

ist es unentschieden?
    - feld füllen ohne zu gewinnen muss unentschieden anzeigen


Testfall-ID: VG-001
Testbeschreibung: spalte 1, 2, 3, 4 gleiche steine hineinwerfen das es eine reihe ergibt

Vorbedingungen:
Das Spiel ist gestartet.
Spieler 1 setzt die vorgegebene Felder 
spieler 2 setzt nicht in den weg

Erwartetes Ergebnis:
Das System zeigt an das gewonnen wurde





Testfall-ID: VG-002
Testbeschreibung: in spalte 1 werden 4 gleiche steine hineingeworfen

Vorbedingungen:
Das Spiel ist gestartet.
Spieler 1 setzt die vorgegebene Felder 
spieler 2 setzt nicht in den weg

Erwartetes Ergebnis:
Das System zeigt an das gewonnen wurde




Testfall-ID: VG-003
Testbeschreibung: diagonale testen mit gleichen steinen

Vorbedingungen:
Das Spiel ist gestartet.
Spieler 1 setzt seine steine diagonal
spieler 2 setzt so das spieler ein diagonal gewinnen kann

Erwartetes Ergebnis:
Das System zeigt an das gewonnen wurde




Testfall-ID: VG-004
Testbeschreibung: Testfälle VG-001, VG-002, VG-003 sollen innerhalb des feldes geprüft werden

Vorbedingungen:
es sind testfall VG-001, VG-002, VG-003 abgeschlossen

Erwartetes Ergebnis:
Das System zeigt an das gewonnen wurde






Testfall-ID: VG-005
Testbeschreibung: Das Feld wird gefüllt so das keiner gewinnt bis das Feld voll ist

Vorbedingungen:
Das Spiel ist gestartet

Erwartetes Ergebnis:
Das System zeigt an das Unentschieden gespielt wurde