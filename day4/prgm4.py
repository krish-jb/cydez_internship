# Arrange string characters such that lowercase letters should come first

string = input("Enter a string: ")
chars = list(string)
chars.sort(reverse=True)
string = "".join(chars)
print(string)
