import re
from typing import Container
import requests
from bs4 import BeautifulSoup as bs
from requests.models import parse_url

url = requests.get("https://www.worldometers.info/coronavirus/").text

web = bs(url, 'html.parser')

nama_negara = []
total_kasus = []
total_kematian = []
total_sembuh = []
kasus_aktif = []
total_dites = []
populasi = []

tugas = [nama_negara, total_kasus, total_kematian, total_sembuh, kasus_aktif,
total_dites, populasi]

table = web.find('tbody').find_all('tr')
table_data = [baris.find_all('td') for baris in table][8:]

# PRACTICE SELF 

""" def NaN_remover(listing, new_list):
    for j in listing:
        if j == 'NaN' or j == '':
            j = 0
        else : 
            j = int(j.text.replace(',', ''))
        new_list.append(j)

print(table_data[8])
 """

for i in table_data:
    nama_negara.append(i[1].text)
    total_kasus.append(int(i[2].text.replace(',', '')))
    total_kematian.append(int(i[4].text.replace(',', '')))
    total_sembuh.append(int(i[6].text.replace(',', '')))
    kasus_aktif.append(int(i[8].text.replace(',', '')))
    total_dites.append(int(i[12].text.replace(',', '')))
    populasi.append(int(i[-5].text.replace(',', '')))

for i in total_kasus:
    print(i)