from datetime import datetime


def dni_do_urodzin(data_urodzin):
    urodziny = datetime.strptime(data_urodzin, "%Y-%m-%d")
    dzis = datetime.now()
    if dzis.month == urodziny.month and dzis.day == urodziny.day:
        print("100 lat")
    else:
        ile_dni = (dzis - urodziny).days
        print(f" od twoich urodzin minelo {ile_dni} dni")
        ile_godzin = (dzis - urodziny).total_seconds() / 3600
        print(f"od twoich urodzin minelo {ile_godzin} godzin ")


def main():
    print(dni_do_urodzin("2023-01-01"))


if __name__ == '__main__':
    main()
