# Python program to remove blank space from string.

string = "Hello, World"
string = "".join(i for i in string if i != ' ')
print(string)