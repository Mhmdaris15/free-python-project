# from bs4 import BeautifulSoup

# with open('HTML File.html', 'r') as html:
#     content = html.read() # read html file

#     soup = BeautifulSoup(content, 'lxml') # to neat html code --> delete indentation of html tag

#     course_html = soup.find_all('h5') # for get all of 'h5' tag
#     # for course in course_html:
#     #     print(course.text) # text method uses for get result without tag html
    
#     course_cards = soup.find_all('div', class_='card')
#     for course in course_cards:
#         print(course.h5.text) # to show h5 result in div tag (title course card)
#         print(course.a.text) # to show a href result in div tag (price course card)
#         print(course.a.text.split()[-1], '\n') # to take the last a href result (only number of price)





from bs4 import BeautifulSoup

with open('HTML File.html', 'r') as html_file:
    konten = html_file.read()

    soup = BeautifulSoup(konten, 'lxml')

    judul = soup.find('h1').text
    
    all_kursus = soup.find_all('div', class_='card')
    title_kursus = soup.find('div', class_='card-body')
    # print(title_kursus)
    for i in all_kursus:
        print(f'Title\t\t:{i.h5.text} \nDescription\t:{i.p.text} \nPrice\t\t:{i.a.text} \n')