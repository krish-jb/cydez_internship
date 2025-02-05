# Reverse each word of a string

string = input("Enter a string: ")
words = string.split()
words = [word[::-1] for word in words]
string = " ".join(words)
print(string)