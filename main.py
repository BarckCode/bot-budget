# Python Core
from datetime import date

# Internal Modules
from excel.excel_controller import Controller


today = date.today()

# Data Excample
initial_balance = 1000

# expenses = (' ', 60, today)

income = ('100', ' ', '2020-09-07')


def type_of_data():
    try:
        return expenses
    except:
        return income


def main():
    data = type_of_data()

    excel = Controller()
    excel.add_data_to_excel(initial_balance, data)


if __name__ == '__main__':
    main()