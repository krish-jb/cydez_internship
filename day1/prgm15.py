# Write a program to convert a string of numbers into a list of integers.
str_numbers = "10 30 40 50 60"
int_numbers = list(map(int, str_numbers.split(" ")))
print(int_numbers)