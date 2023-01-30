class Animal:

    def oddychaj(self):
        print("oddycham")

    def spij(self):
        print("spie")

    def przedstaw_sie(self):
        print("hej")


class Kot(Animal):
    def spij(self):
        print("mrr spie jak kot")

    def miaucz(self):
        print("miau")


class Pies(Animal):
    def oddychaj(self):
        print("dysze....")

    def szczekaj(self):
        print("hau")


class Slimak(Animal):
    def przedstaw_sie(self):
        print("jestem slodkim slimakiem")


kot = Kot()
pies = Pies()
slimak = Slimak()

zwierzeta = [pies, kot, slimak]

for zwierze in zwierzeta:
    zwierze.przedstaw_sie()
    zwierze.spij()
    zwierze.oddychaj()
    print()
