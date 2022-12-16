# python-kodtoro_egyszeru

Folyamatleírás:


1. játékszabályok rögzítése, a program feladatainak specifikálása

2. fő részekre bontás:
  - inicializálás
  - játék

2.1. inicializálási rész alrészekre bontása
  - változók beállítása
  - feladvány generálása (színek elrejtése)

    2.1.2 feladvány generálása
        Addig generálunk véletlenszerűen színeket, amíg a listán 4 különböző szín lesz.
        Tehát ami egyszer már szerepel rajta, nem adjuk hozzá mégegyszer.
2.2 játék
   - ismétlés, amíg a játékos kitalálja a feladványt vagy a maximális lépésszámot meghaladja.

   2.2.1 a játék ciklusa:
        - tippelés
        - tipp validálása (érvényes-e?)
        - tipp kiértékelése (hány találat volt, ami nem volt jó helyen,
          és hány találat volt, ahol a hely is helyes volt)
        - tipp rögzítése
        - játék végellenőrzése (a játék valamelyik végkifejlete megvalósult-e)

    2.2.1.1 tippelés
        - adatbekérés a játékostól
    2.2.1.2  (formai) ellenőrzés:
          - négy karakter hosszú-e
          - csak a megadott karaktereket tartalmazza-e
          - minden karaktert csak egyszer tartalmaz-e
    2.2.1.3 tipp kiértékelése
          - érvényes tipp esetén (ha az előző pont igaz értékkel tér vissza) ciklussal végigmegyünk a tipp karakterein
          - ellenőrizzük, hogy az tipp aktuálisan vizsgált karaktere (akt. karakter) 
            egyezik-e a feladvány ugyanazon pozíciójában található színnel, ha igen \+1 pozíció találat
            egyébként megtalálható-e a feladvány karakterei között az akt. karakter?
            ha igen \+1 szín találat
    2.2.1.4 tipp rögzítése
          - a tippek számának növelése
          - opcionálisan a tipp rögzítése egy listán
    2.2.1.5 a játék végének vizsgálata
          - ha a játékos utolsó tippje 4 helyes pozíciós volt -> nyert
          - ha az utolsó tipp a 10. volt, de nem 4 helyes pozíciós volt -> vesztett
