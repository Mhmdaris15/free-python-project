import re
from typing import Text
import requests
from bs4 import BeautifulSoup


url = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35').text

soup = BeautifulSoup(url, 'lxml')

# find_all --> matches all of the precious tag
# find --> matches only the first tag
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

# USING FOR LOOP
# for i in jobs:
#     sub_com = i.find('h3', class_='joblist-comp-name').text.replace(' ', '').replace('\r', '').replace('\n', '')
#     company_name.append(sub_com)

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>>')
print('Filtering out : ' + unfamiliar_skill)

# USING LIST COMPREHESION
publised_day = [i.find('span', class_='sim-posted').span.text for i in jobs]
company_name = [i.find('h3', class_='joblist-comp-name').text.replace(' ', '').replace('\r', '').replace('\n', '') for i in jobs]
skills = [i.find('span', class_='srp-skills').text.replace(' , ', ',').replace(' ', '') for i in jobs]
more_info = [i.header.h2.a['href'] for i in jobs]

for i in range(len(company_name)):
    if '1' in publised_day[i] and unfamiliar_skill not in skills[i]:
        print(f'''
        Company : {company_name[i].strip()}
        Skill Required : {skills[i].strip()}
        More Info : {more_info[i]}
        ''')


# for (i,j) in zip(company_name, skills):
#     print(f'Company : {i} \nSkill : {j}')