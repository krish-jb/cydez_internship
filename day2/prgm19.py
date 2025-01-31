# Find the factorial of a given number
def fact(number):
    if number > 1:
        return number * fact(number - 1)
    return 1
number = int(input("Enter a number: "))
print(fact(number))

