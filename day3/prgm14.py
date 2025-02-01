# Write a Python function that takes a number as a parameter and check the number is prime or not.


def is_prime(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
print(f"{number} is {"" if is_prime(number) else "not "}a prime number")
