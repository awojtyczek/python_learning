wiek = input("ile masz lat? ")
wiek = int(wiek)
if wiek > 30:
    print("lata leca")
elif wiek <= 0:
    raise ValueError("nie moze byc ujemna")
else:
    print('mlodosc nie wiecznosc')


