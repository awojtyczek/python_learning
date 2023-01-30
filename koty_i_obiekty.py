from klasy_osobno import Kot, Food


def main():
    kot1 = Kot("Ryan", 6)
    kot2 = Kot("Prinsio", 7)
    kot3 = Kot("Colin", 2)

    jedzenie1 = Food("kurczak", 400, True)
    jedzenie2 = Food("kabanosy", 300, True)
    jedzenie3 = Food("czekolada", 600)
    jedzenie4 = Food("kefir", 200, True)

    kot1.biegaj()
    kot1.spij()
    kot1.spij()
    kot1.spij()
    kot1.zjedz(jedzenie4)
    kot1.zjedz(jedzenie3)
    print(kot1.co_zjadl_kot())


if __name__ == '__main__':
    main()
