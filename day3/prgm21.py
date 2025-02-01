# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).

def square(start=1, end=30):
    list_ = [i ** 2 for i in range(start, end + 1)]
    print(list_)
    
square()