import requests
from bs4 import BeautifulSoup
from requests.models import parse_url

result = requests.get('https://www.globalfirepower.com/countries-listing.asp')
# print(result)

# print(result.status_code)

# print(result.headers)

res_content = result.content

soup = BeautifulSoup(res_content, 'lxml')

point_table = soup.find_all('div', class_='contentStripOuter')[3]

point_table = point_table.find_all('a')

countries = []
for i in point_table:
    i = i.text
    i = i.replace('\n', '')
    i = i.replace('\t', '')
    countries.append(i)

print(countries)