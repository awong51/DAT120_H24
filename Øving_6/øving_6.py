import csv
import re
from datetime import datetime
def get_value(file_name,key_name): #returns the value of temp or pressure 
    list_temp = []
    with open(file_name,encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            list_temp.append(row[key_name])
    return list_temp

def get_time(file_name,key_name, convert): #returns the date in [day, month, year, hour, minute] format. The 'convert' value is either true when '== True' or false when '== False' 
    list_temp = []
    with open(file_name,encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            x = re.split(r'[. :]', row[key_name])
            if convert == True: #changes format from month first to day first
                x = x[1],x[0],x[2],x[3],x[4]
            try:
                list_temp.append(list(map(int,x))) #will stop when format isnt only numbers and in this case will stop when its not [day, month, year, hour, minute]
            except:
                break
    return list_temp

print(get_value('Sola_vær.csv', 'Lufttemperatur'))

#print(get_time('Sola_vær.csv', 'Tid(norsk normaltid)', False))