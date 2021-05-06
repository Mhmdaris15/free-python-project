
def recursion_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursion_fibonacci(n-1) + recursion_fibonacci(n-2)

n_terms = int(input('Input n_terms : '))

# Check if the number is valid
if n_terms <= 0:
    raise ValueError
else:
    print('Fibonacci Series:')
    for i in range(1, n_terms):
        print(recursion_fibonacci(i))

def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n-1)

num = int(input('Input n_factorial : '))
if num < 0:     
    print("Invalid input ! Please enter a positive number.")   
elif num == 0:   
    print("Factorial of number 0 is 1")   
else:   
    print("Factorial of number", num, "=", factorial(num))