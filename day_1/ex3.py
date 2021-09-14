# ITP Week 4 Day 1 Exercise

# https://data.messari.io/api/v2/assets


import requests
import json
import openpyxl
from openpyxl.styles import Font


data = requests.get('https://data.messari.io/api/v2/assets')
beautify = json.loads(data.text)

symbol = beautify['data']

roi = beautify['data'][0]['metrics']['roi_data']['percent_change_last_1_week']

# print(roi)
# print(symbol)


wb = openpyxl.load_workbook('/Users/alexjacobo/Desktop/vit/intropython/week4/itp_week_4/day_1/output.xlsx')

sheet = wb['Sheet1']

sheet['A1'] = "Symbol"
sheet['A1'].font = Font(bold=True)
sheet['B1'] = 'ROI'
sheet['B1'].font = Font(bold=True)

sym_counter = 0
sheet_counter = 2

for index in range(20):
    symbol_list = beautify['data'][sym_counter]['symbol']
    sheet['A' + str(sheet_counter)] = symbol_list
    sheet_counter += 1
    sym_counter += 1


sheet2_counter = 2
roi_counter = 0

for item in range(20):
    roi_list = beautify['data'][roi_counter]['metrics']['roi_data']['percent_change_last_1_week']
    sheet['B' + str(sheet2_counter)] = roi_list
    sheet2_counter += 1
    roi_counter += 1


wb.save('/Users/alexjacobo/Desktop/vit/intropython/week4/itp_week_4/day_1/output.xlsx')
