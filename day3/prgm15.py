"""
Create an inner function to calculate the addition in the following way
              Create an outer function that will accept two parameters, a and b
              Create an inner function inside an outer function that will calculate the addition of a and b
              At last, an outer function will add 5 into addition and return it
"""


def add(num1, num2):
    def _add():
        return num1 + num2

    return _add() + 5


print(add(5, 10))
