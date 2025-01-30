# Write a program to find the largest number out of three numbers excepted from user.

num1 = int(input("Enter three space separated numbers: "))
num2 = int(input())
num3 = int(input())
big = num1
if num2 > big:
    big = num2
if num3 > big:
    big = num3
print(f"Biggest number is {big}")

