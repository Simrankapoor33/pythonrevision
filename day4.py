def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
n = 5
print(f"The factorial of {n} is:", factorial(n))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage
num = 7
print(f"Is {num} a prime number? {is_prime(num)}")

def add_numbers(a, b=10):
    return a + b

# Example usage
result1 = add_numbers(5)
result2 = add_numbers(5, 7)
print(f"The sum of 5 and default 10 is: {result1}")
print(f"The sum of 5 and 7 is: {result2}")