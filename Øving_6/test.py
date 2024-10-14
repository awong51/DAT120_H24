import csv
import re
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
def get_value(file_name,key_name): #returns the value of temp or pressure 
    list_temp = []
    with open(file_name,encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            list_temp.append(row[key_name].split(',')[0])
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


'''print(get_value('UiS_vær.csv', 'Temperatur (gr Celsius)')) >>> 17

print(get_value('Sola_vær.csv', 'Lufttemperatur')) >>> 17

print(get_value('UiS_vær.csv', 'Trykk - absolutt trykk maaler (bar)')) >>> 100

print(get_value('Sola_vær.csv', 'Lufttrykk i havnivå')) >>> 100

print(get_time('Sola_vær.csv', 'Tid(norsk normaltid)')) >>> [x,x,x,x,x] dag,måned,år,time,minutt

print(get_time('UiS_vær.csv', 'Dato og tid')) [x,x,x,x,x] '''

def get_time_graph(csv, key_tid, key_temp, convert):        
    tid_sted = get_time(csv,key_tid, convert)
    temp_sted = get_value(csv,key_temp)
    
    print(tid_sted[0])
    print(tid_sted[-1])
    x_values = []
    y_values = []
    for i in range (len(tid_sted)):
        
        x_values.append(datetime(tid_sted[i][2],tid_sted[i][1],tid_sted[i][0],tid_sted[i][3],tid_sted[i][4]))
        y_values.append(int(temp_sted[i]))

    plt.plot(x_values, y_values)



get_time_graph('Sola_vær.csv', 'Tid(norsk normaltid)', 'Lufttemperatur', False)

get_time_graph('UiS_vær.csv', 'Dato og tid', 'Temperatur (gr Celsius)', True)

plt.show()