import math

# Define function
def prime_checker(num):
    check_result = f"{num} is a prime number!"
    max_divider = math.ceil(math.sqrt(num))
    for divider in range(2, max_divider + 1):
        if num % divider == 0:
            check_result = f"{num} is not a prime number!"
            break
    print(check_result)

# Take input and call the function
n = int(input("Check this number: "))
prime_checker(n)