# Write a Python function that prints out the first n rows of Pascal's triangle


def fact(number):
    if number > 1:
        return number * fact(number - 1)
    return 1


row_count = 5
for row in range(row_count):
    for col in range(row + 1):
        print(int(fact(row) / (fact(col) * fact(row - col))), end=" ")
    print()
