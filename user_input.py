def zapytaj_uzytkownika_o_imie():
    return input("podaj swoje imie: ")


def przywitaj_ryana():
    print("siema maly bandyto")


def przywitaj_prinsia():
    print("witaj slodki grubasku")


def przywitaj_innego_kota(kot):
    print(f"chyba sie jeszcze nie znamy kocie {kot}, milo cie poznac")


def is_kot_ryan(kotek):
    return kotek == "Ryan"


def is_kot_prinsio(kotek):
    return kotek == "Prinsio"


def main():
    imie_kota = zapytaj_uzytkownika_o_imie()

    if is_kot_ryan(imie_kota):
        przywitaj_ryana()
    elif is_kot_prinsio(imie_kota):
        przywitaj_prinsia()
    else:
        przywitaj_innego_kota(imie_kota)


if __name__ == '__main__':
    main()
