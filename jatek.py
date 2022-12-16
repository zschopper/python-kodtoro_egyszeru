import random

'''
K - Kék,
S - Sárga,
Z - Zöld,
P - Piros,
N - Narancs,
F - Fehér
'''

def elrejt(rejtett):
    szinek = 'KSZPNF'
    while len(rejtett) < 4:
        szin = szinek[int(random.random() * 6)]
        if szin not in rejtett:
            rejtett.append(szin)

# Ellenőrzés feladata:
# - négy, egymástól különböző, érvényes színkód kell
def tipp_vizsgal(tipp):

    szinek = 'KSZPNF'

    # Pozitív eredménnyel kezdünk, ha valahol hibát találunk a tippben, ezt állítjuk False-ra.
    # A függvény ezt a változót adja vissza a visszatérési értékében
    eredmeny = True

    # Egy gyors ellenőrzés - ha nem 4 karakter hosszú a tipp, már nem is nézzük tovább, hibás.
    if len(tipp) != 4:
        eredmeny = False
    else:
        i = 0
        # végiglépkedünk a tipp karakterein, és ellenőrizzük, hogy
        # - csak érvényes színkódokat tartalmaz-e
        # - egy színt csak egyszer tartalmaz-e
        while eredmeny and i < 4 and tipp[i] in szinek:
            j = 0

            karakter_elofordulas = 0
            # többször megadott színek ellenőrzése - a külső ciklus aktuális színének
            # előfordulását keressük a tippben, ha ez nem 1, akkor többször van benne, ami hiba
            while j < 4:
                if tipp[i] == tipp[j]:
                    karakter_elofordulas += 1

                j += 1

            if karakter_elofordulas != 1:
                eredmeny = False

            i += 1
    return eredmeny

# add kérünk be tippeket, amíg nyer vagy veszít a játékos
def jatek(rejtett):
    # A játék addig folytatódik, amíg 10 vagy kevesebb tippünk van, ÉS az utolsó tipp nem 4 jó pozíciós
    tippek = 0
    # a tippek vizsgálatánál a poz változóban tároljuk azokat a találatokat, ahol a pozíció is jó.
    # ha a vizsgálat eredménye poz == 4, akkor a játékos nyert, a játék véget ért.
    poz = 0

    while tippek < 10 and poz != 4:
        tipp = input('Mi a tipped? ').upper()
        if tipp_vizsgal(tipp):
            i = 0
            poz = 0  # ebben tároljuk azokat a találatokat, ahol a szín ÉS a hely is jó
            szin = 0  # ebben tároljuk azokat a találatokat, ahol a szín jó, de a hely nem.
            while i < 4:
                if tipp[i] == rejtett[i]:  # jó pozíció
                    poz += 1
                elif tipp[i] in rejtett:  # jó szín
                    szin += 1
                i += 1
            tippek += 1
            print(f"{tippek}. tipp: {szin} találat, {poz} jó helyen")
        else:
            print("Hibás tipp")
    if poz == 4:
        print("Nyertél")
    else:
        print("Veszítettél, a megoldás", ", ".join(rejtett), "volt")
