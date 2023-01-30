wiek = input("ile masz lat? ")
try:
    wiek = int(wiek)
except:
    print("sorry, to nie jest liczba")
    exit()

if wiek > 30:
    print("lata leca")
elif wiek <= 0:
    raise ValueError("nie moze byc ujemna")
else:
    print('mlodosc nie wiecznosc')

