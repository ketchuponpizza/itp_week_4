import requests
import json
import openpyxl

data = requests.get('https://data.messar.io/api/v2/assets')
beautify = json.loads(data.text)

#print(beautify)
symbol = beautify['data'][0]['symbol']

roi = beautify['data'][0]['metrics']['roi_data']['percent_change_last_1_week']

#print(data)

# print(roi)
# print(symbol)
# for i in data


wb = openpyxl.load_workbook('./output.xlsx') # use absolute path

sheet = wb['Sheet1']

sheet['A1'] = "Symbol"
sheet['B1'] = "ROI"


# for index in beautify:
#     symbol = index['symbol']
#     # counter += 1

sym_counter = 0
sheet_counter = 2

for index in range(20):
    symbol_list = beautify['data'][sym_counter]['symbol']
    sheet['A' + str(sheet_counter)] = symbol_list
    sheet_counter += 1
    sym_counter += 1
    print(symbol_list)
sheet2_counter = 2
roi_counter = 0
for item in range(20):
    roi_list = beautify['data'][roi_counter]['metrics']['roi_data']['percent_change_last_1_week']
    roi_counter += 1
    print(roi_list)



wb.save('./output.xlsx') # use absolute path

# print(symbol_list)


