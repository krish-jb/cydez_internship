# Write a Python function to find the Max of three numbers.

def max3(num1, num2, num3):
    big = num1
    if num2 > big:
        big = num2
    if num3 > big:
        big = num3
    return big


num1 = -1
num2 = 0
num3 = 2
print(max3(num1, num2, num3))
