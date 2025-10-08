trenutnoStanje = 0
def main():
    while True:
        print("**Welcome to the bank!**")
        print("Pritisnite 1 da pristupite aplikaciji")
        print("Pritisnite 0 da izadjete iz programa")
        #userinput
        try:
            userInput1 = int(input("Unesite broj 1 ili 0: "))
            #ako je unet broj 1 imamo nove opcije
            if userInput1 == 1:
                while True:
                    print("Pritisnite 2 da vidite stanje racuna")
                    print("Pritisnite 3 da uplatite novac na racun")
                    print("Pritisnite 4 da prebacite novac na tudj racun")
                    print("Pritisnite 5 da biste podigli novac sa racuna")
                    print("Pritisnite 6 da se vratite na pocetni ekran")
                    #unos broj 2
                    try:
                        userInput2 = int(input("Unesite broj 2-6: "))
                        #ako je unet broj 2
                        if userInput2 == 2:
                            StanjeNaRacunu()
                        #ako je unet broj 3
                        elif userInput2 == 3:
                            uplatiNovac()
                            StanjeNaRacunu()
                        elif userInput2 == 4:
                            prebaciNovac()
                            StanjeNaRacunu()
                        elif userInput2 == 5:
                            podigniNovac()
                            StanjeNaRacunu()
                        elif userInput2 == 6:
                            break
                        else:
                            print("Unos mora biti od 2 do 6")
                    except ValueError:
                        print("Unos mora biti broj")
            elif userInput1 == 0:
                print("Izlazim iz programa")
                break
            else:
                print("Unos mora biti 1 ili 0")
        except ValueError:
            print("Unos mora biti broj")
#funkcije
def uplatiNovac():
    global trenutnoStanje
    print("Koliko novca zelite da uplatit na Vas racun?")
    try:
        dodajNovac = float(input("Unesite iznos: "))
    except ValueError:
        print("Unos mora biti broj")
    trenutnoStanje += dodajNovac
    

def podigniNovac():
    global trenutnoStanje
    print("Koliko novca zelite da podignete?")
    try:
        podigni = float(input("Unesite iznos koji zelite da podignete sa svog racuna: "))
    except ValueError:
        print("Unos mora biti broj")
    if podigni > trenutnoStanje:
        print("Greska, nemate dovoljno novca na racunu")
    else:
        trenutnoStanje -= podigni

def StanjeNaRacunu():
    global trenutnoStanje
    print(f"Trenutno stanje na Vasem racunu je: {trenutnoStanje}")
def prebaciNovac():
    global trenutnoStanje
    print("Koliko novca zelite da prebacite?")
    try:
        prebaci = float(input("Unesite iznos koji zelite da prebacite: "))
    except ValueError:
        print("Unos mora biti broj")
    if prebaci > trenutnoStanje:
        print("Nemate dovoljno novca na racunu")
    else:
        trenutnoStanje -= prebaci
        print(f"Uspesno ste prebacili: {prebaci}")

main()