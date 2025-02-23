
"""
num =int(input("enter the number you want to check"))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")    
    
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")
    
N = int(input("Enter an integer N: "))
sum_natural_numbers = 0

for i in range(1, N + 1):
    sum_natural_numbers += i

print("The sum of the first", N, "natural numbers is:", sum_natural_numbers)

num = int(input("Enter an integer: "))

print(f"Multiplication table of {num}:")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

N = int(input("Enter an integer N: "))
i = 1

while i <= N:
    print(i)
    i += 1    

    
num = int(input("Enter an integer: "))
reverse_num = 0

while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10

print("The reverse of the number is:", reverse_num)

N = int(input("Enter the number of Fibonacci numbers to generate: "))

a, b = 0, 1
count = 0

while count < N:
    print(a)
    a, b = b, a + b
    count += 1
    """
num = int(input("Enter an integer: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")