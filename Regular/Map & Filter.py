from functools import reduce 

nums = "12 13 23 36 45 67 98 90 101 65".split()
nums = list(map(int, nums))

even_num = list(filter(lambda x: x % 2 == 0, nums))
print(nums, even_num, sep='\n')

my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = list(map(str.upper, my_pets))
print(uppered_pets)

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
rounded_areas = list(map(lambda x: round(x, ndigits=2), circle_areas))
print(rounded_areas)

teen_areas = list(filter(lambda x: x<10 and x>3, circle_areas))
print(teen_areas)
# ALL() and ANY()

lst = list(map(int,('1 3 4 6 7 9'.split())))
print(lst)
if all(lst) < 10:
    print('Your numbers are less than 10')
if any(lst) >= 1:
    print('There is 1 in your list')

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda x: x == x[::-1], dromes))
print(palindromes)

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
grater_75 = list(filter(lambda x: x >= 75, scores))
print(grater_75)


numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second
# >> 68
result = reduce(custom_sum, numbers)
print(result)

"EXERCISE !"

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than 
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: x**2, my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers[-2:])

print(map_result)
print(filter_result)
print(reduce_result)