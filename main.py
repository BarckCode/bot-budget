# Packages
import openpyxl


# Data
money_flow = [
    (' ', 750, '2020-09-05'),
    (' ', 10, '2020-09-06'),
    (' ', 60, '2020-09-07'),
]

# Inicialize Workbook
wb = openpyxl.Workbook()

# Create Sheet
sheet = wb.active
sheet.title = 'Control de Gastos'

# Initial Balance
sheet.append(('Saldo inicial:', 1000))


# Create Header
sheet.append(('Ingresos', 'Gastos', 'Fecha'))


for data in money_flow:
    # Tuple with values
    sheet.append(data)


# Save Workbook
wb.save('money_control.xlsx')