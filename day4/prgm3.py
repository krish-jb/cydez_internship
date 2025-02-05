# Create a string made of the first, middle and last character

string = input("Enter a string: ")
result = string[0] + string[len(string) // 2] + string[-1]
print(result)
