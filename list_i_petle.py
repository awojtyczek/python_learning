koty = []
while True:
    imie = input("jak sie nazywasz ?")
    if imie == "tyle":
        break
    print(f"witamy {imie}")
    koty.append(imie)
    print(koty)

    if imie == "Prinsio":
        print("siemka grubasie")

for kot in koty:
    print(f"siema kocie {kot}")
    if kot == "Prinsio":
        print("siema grubasie")