from datetime import datetime


def sprwadz_date_waznosci(data_waznosci):
    obecna_data = datetime.now().date()
    return obecna_data > data_waznosci


def main():
    data_jako_string = input("podaj date waznposci (YYYY-MM-DD):  ")
    moja_data = datetime.strptime(data_jako_string, "%Y-%m-%d").date()

    print(moja_data)
    print(sprwadz_date_waznosci(moja_data))


if __name__ == '__main__':
    main()
