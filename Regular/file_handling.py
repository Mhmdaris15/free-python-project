import os
# os.remove('Code Cheat GTA.docx')


if os.path.exists('Code Cheat GRA.docx'):
    os.remove('Code Cheat GRA.docx')

# os.rmdir("myfolder") # To delete the entire folder

# WITH STATEMENT to get code became cleaner

with open('filename.txt', 'w') as file:
    file.write('Halo nama saya aris\n')
    file.write('Ini penulisan kedua saya\n')
    file.write('dan ini penulisan ketiga saya')
    file.close()

with open('filename.txt', 'rt') as file:
    print(file.read())
    file.close()

# WITHOUT WITH STATEMENT

f = open('filename.txt', 'r')
r = f.readlines()
print(r)
f.close()

# WITHOUT WITH STATEMENT 2ND

fi = open('filename.txt', 'w')
try:
    fi.write('Ini adalah tulisan terakhir saya')
finally :
    fi.close()

# EXCEPTION ERROR

try:
    print(1)
    assert 2+2==5
except AssertionError:
    print('exception error has exist')
except:
    print('just try your best')

