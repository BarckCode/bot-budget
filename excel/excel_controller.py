# Python Core
import os.path

# Excel Library
import openpyxl


class Controller:
    """
    Class that handles excel books
    """

    def __init__(self):
        self.wb = openpyxl.Workbook()   # Inicialize Workbook


    def check_excel_exist(self):
        excel_exist = os.path.isfile('money_control.xlsx')

        if excel_exist:
            return True     # Excel Exist
        else:
            return False    # Excel doesn't Exist


    def add_data_to_excel(self, initial_balance, data):
        exist = self.check_excel_exist()
        if exist:
            pass
        else:
            sheet = self.wb.active              # Active Sheet
            sheet.title = 'Control de Gastos'   # Rename Sheet


            initial_data = [
                ('Saldo inicial:', initial_balance),    # Initial Balance
                (' ',),                                 # Blank Space
                ('Ingresos', 'Gastos', 'Fecha'),     # Sheet Header
            ]

            # Add Initial Data
            for tuple_data in initial_data:
                sheet.append(tuple_data)

            # Add Expenses or Income
            sheet.append(data)

        # Save Excel
        self.wb.save('money_control.xlsx')