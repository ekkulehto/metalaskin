# määritellään metaluokka, joka muokkaa luokkan määrittelyä ennen sen luontia
class Metaluokka(type):
    # yliajetaan luokan luontiprosessi (__new__ -metodi)
    def __new__(cls, clsname, bases, clsdict):
        print("____________________________________________")
        print(f"| Metaluokka luo ja rakentaa luokan {clsname} |")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

        # määritellään laskimen funktiot (esimerkin vuoksi metaluokan sisällä)
        def summa(a, b): return a + b
        def erotus(a, b): return a - b
        def tulo(a, b): return a * b
        def osamäärä(a, b): return a / b

        # käydään läpi lista jossa on lisättävän funktion nimi ja itse funktio
        for name, func in [
            ("summa", summa),
            ("erotus", erotus),
            ("tulo", tulo),
            ("osamäärä", osamäärä),
        ]:
            # kääritään funktio dekoraattorilla ja lisätään se Laskin-luokalle
            clsdict[name] = dekoraattori(func)

        # palautetaan lopullinen luokka, joka sisältää uudet funktiot
        return super().__new__(cls, clsname, bases, clsdict)


def dekoraattori(func):
    # dekoraattori käärii alkuperäisen funktion ja käsittelee sen tulostuksen

    def kääritty_alkuperäinen_funktio(*args, **kwargs):

        # tulostetaan laskutoimituksen kuvaus annetuilla argumenteilla ja funktion nimellä
        print(
            f"Lukujen {args} {func.__name__} on ", end="")

        # kutsutaan alkuperäistä funktiota ja palautetaan sen laskutoimituksen tulos
        return func(*args, **kwargs)

    # palautetaan uusi kääritty funktio
    return kääritty_alkuperäinen_funktio


class Laskin(metaclass=Metaluokka):
    # metaluokka lisää tänne dekoraattorilla käärityt laskutoimitukset automaattisesti
    pass


# pääohjelmana yksinkertainen laskinsovellus
if __name__ == "__main__":
    # kysytään käyttäjältä haluttu laskutoimitus
    while True:
        print("Valitse laskutoimitus [enter lopettaa]")
        print("1: summa")
        print("2: erotus")
        print("3: tulo")
        print("4: osamäärä\n")

        # luetaan käyttäjän valinta
        valinta = input("Valinta: ")

        # enter lopettaa
        if valinta == "":
            print("Kiitos ja kuulemiin!")
            break

        # varmistetaan kelvollinen valinta
        elif valinta not in ["1", "2", "3", "4"]:
            print("Anna kelvollinen laskuoperaatio!\n")
            continue

        # kysytään käyttäjältä laskutoimitukseen luvut
        try:
            eka_luku = int(input("Anna ensimmäinen luku: "))
            toka_luku = int(input("Anna toinen luku luku: "))

            # kutsutaan valittua laskutoimitusta (jotka metaluokka on lisännyt laskimeen)
            match valinta:
                case "1":
                    print(Laskin.summa(eka_luku, toka_luku))
                case "2":
                    print(Laskin.erotus(eka_luku, toka_luku))
                case "3":
                    print(Laskin.tulo(eka_luku, toka_luku))
                case "4":
                    print(Laskin.osamäärä(eka_luku, toka_luku))

        # virheenkäsittely
        except ValueError:
            print("Anna kokonaisluku!")
        except ZeroDivisionError:
            print("'nollalla ei voi jakaa!'")

        print("____________________________________________\n")
