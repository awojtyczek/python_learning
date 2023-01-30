wynik = []
lista = list(range(1, 30))

print("zwykla petla")

for liczba in lista:
    if liczba % 2 == 0:
        wynik.append(liczba ** 2)

print(wynik)

print("list comprehension")

wynik2 = [liczba ** 2 for liczba in lista if liczba % 2 == 0]
print(wynik2)
