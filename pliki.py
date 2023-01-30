def main():
    plik = open("koty.txt", "r")
    koty = []

    for kot in plik:
        koty.append(kot.strip().upper())

    plik2 = open("duzeKoty.txt", "w")

    for kot in koty:
        plik2.write(kot + "\n")

    plik.close()
    plik2.close()


if __name__ == '__main__':
    main()
