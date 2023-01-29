
class Food:
    def __init__(self, nazwa_jedzenia, ilosc_kalorii, czy_jadalne_dla_kota=False):
        self.nazwa_jedzenia=nazwa_jedzenia
        self.ilosc_kalorii=ilosc_kalorii
        self.czy_jadalne_dla_kota=czy_jadalne_dla_kota

    def description(self):
        print(f"jedzenie dla kota to: {self.nazwa_jedzenia}, ilosc kalorii: {self.ilosc_kalorii}, czy jadalne dla kota: {self.czy_jadalne_dla_kota}")

    def __repr__(self):
        return f"{self.nazwa_jedzenia}"

    def __eq__(self, other): # potrzebne do porownywania czy obiekty są takie same
        if isinstance(other, Food):
            return self.nazwa_jedzenia == other.nazwa_jedzenia
        return False

    def __hash__(self): # potrzebne do uzywania w slowniku / dictionary
        return hash(self.nazwa_jedzenia)


class Kot:
    def __init__(self, imie, wiek):
        self.imie=imie
        self.wiek=wiek
        self.ilosc_energii=500
        self.zjedzone=[]

    def miaucz(self):
        if self.ilosc_energii<200:
            raise ValueError("kot jest zmeczony i nie ma sily miauczec")
        self.ilosc_energii-=200

    def przedstaw_sie(self):
        return f"{self.imie}, wiek: {self.wiek} lat, \n energia: {self.ilosc_energii} zjadlem dzisiaj {self.zjedzone}"

    def zjedz(self, jedzonko):
        if jedzonko.czy_jadalne_dla_kota:
            print(f"kotek zjadl: {jedzonko}")
            self.ilosc_energii += jedzonko.ilosc_kalorii
            self.zjedzone.append(jedzonko)
        else:
            print("chuj ci w dupe z takim jedzeniem!!!!")


    def biegaj(self):
        if self.ilosc_energii<=0:
            print("kot jest zmeczony i nie ma sily biegac")
            return
        print("kotek sobie biega")
        self.ilosc_energii-=500
        print(f"kot po bieganiu ma {self.ilosc_energii} energii")

    def co_zjadl_kot(self):
        print(F"kotek zjadl: {self.zjedzone}")

    def spij(self):
        if self.ilosc_energii>=500:
            raise ValueError("nie chce mi sie spac, mam za duzo energii")
        self.ilosc_energii+=200

    def mrucz(self):
        if self.ilosc_energii<200:
            print("nie mam ochoty mruczc, bo jestem zly")
            return
        print("mrrr")
        self.ilosc_energii-=100

    def __repr__(self):
        return f"{self.imie}"

