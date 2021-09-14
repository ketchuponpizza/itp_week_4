# psuedo code first 
# break everything down to the smallest pieces
# write and check every pieces

# https://data.messari.io/api/v2/assets

import requests
import json
import openpyxl
#wb = openpyxl.load_workbook("/home/dkayzee/vit/intro-python-august-2021/itp_week_4/day_1/output.xlsx")
#sheet = wb["Sheet1"]


def get_data(url):
    response = requests.get(url)
    # print(response)
    json_result = response.text
    # print(json_result)
    # print(type(json_result))
    clean_data = json.loads(json_result)
    result = clean_data["data"]
    return result

result = get_data("https://data.messari.io/api/v2/assets")

row = 1
symbols = []


def write_data(result):
    global row
    for character in result:
        symbols.append(character['symbol'])


print(symbols)


# sheet['A' + str(row)] = character['id']
#sheet['A' + str(row)] = character['symbol']
# sheet['C' + str(row)] = character['name']
#sheet['D' + str(row)] = character['slug']
#row+=1


# write_data(result)
# wb.save("C:\Users\purub\OneDrive\Desktop\VetsInTech workspace\itp_week_4\day_1\output.xlsx")
