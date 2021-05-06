
print("====BELAJAR DICTIONARY====")
monthConversions = {
    "Jan":"January", #Jan is key, which it is unique
    "Feb":"February", #February is a value
    9:"March", #key bisa berupa angka (int)
    "Apr":"April",
    True:"May", #apa aja bisa jadi key pokoknya
    "Jun":"June", #tapi gabisa ganda ya, INGET!
    "Jul":"July",
    "Aug":"August",
}

print(monthConversions)
print(monthConversions["Jan"])
print(monthConversions.get("Luv", "My name is Aris"))
print(monthConversions[True])




print("====BELAJAR WHILE LOOP====")

i = 1
while i <= 8: #This is a condition
    print(i)
    i += 1 #sama seperti i = i + 1, tapi syntax ini simpler

print("Program already done")




print("====BUILDING A GUESSING GAME====")
print('''===What is the biggest communist country in the world ever===
--> this country is the first communist country in the world ''')
secret_word = "ussr"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("input the answer:")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess :
    print("OUT OF GUESS, YOU LOSE!")
else:
    print("You win!")
