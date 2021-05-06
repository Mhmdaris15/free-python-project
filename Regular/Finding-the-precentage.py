""" def mean(list):
    total = 0
    for i in list:
        total += i
    return (total / len(list))

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
print("{:.2f}".format(mean(student_marks[query_name]))) """
introduce = 'My Name is {name}\nI\'m {age} years old\nNow I study in {school}\nIn {majority} Field' 
print(introduce.format(name='aris', age='17', school='SMKN 1 Cibinong', majority='Computer CS'))

print()

""" print('%s --> AI Mastah'%('Muhammad Aris Septanugroho'))
print('%-15s --> ML Mastah'%('Muhammad Aris Septanugroho'))
print('%.12s --> NE Mastah'%('Muhammad Aris Septanugroho'))
"""
string = "I wondering why my code is %s me. I have longer time to solve the %s"
tipe = 'Bug'
result = 'Troubling'
print(string%(result,tipe))

cost = 70000
site = 'Tokopedia'
kalimat = 'Aku berbelanja di %s dengan diskon sebesar %o(Dalam Oktal Number)'
print(kalimat%(site,cost))

kalimat = 'Aku berbelanja di %s dengan diskon sebesar %X(Dalam Hexadecimal Number)'
print(kalimat%(site,cost))

kalimat = 'Aku berbelanja di %s dengan diskon sebesar %d'
print(kalimat%(site,cost))

print()

kalimah = 'I am buying a {0:s} and using it to rent and earn money. I bought {1:d}!'
print(kalimah.format('Server', 300))