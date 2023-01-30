def main():
    lista_kotow = ["Ryan", "Prinsio", "Ostin"]
    print(lista_kotow)
    lista_kotow.append("Colin")
    print(lista_kotow)
    lista_kotow.insert(0, "Mecio")
    print(lista_kotow)
    print(len(lista_kotow))
    lista_kotow.sort()
    print(lista_kotow)
    lista_kotow.sort(reverse=True)
    print(lista_kotow)
    lista_kotow.remove("Mecio")
    print(lista_kotow)
    del lista_kotow[2]
    print(lista_kotow)
    lista_kotow.clear()
    print(lista_kotow)

    slownik_kotow = {"Ryan": 6, "Prinsio": 7, "Colin": 2}
    print(slownik_kotow)
    print(slownik_kotow["Ryan"])
    slownik_kotow["Ostin"] = 1
    print(slownik_kotow)
    slownik_kotow["Ostin"] = 2
    print(slownik_kotow)


if __name__ == '__main__':
    main()
