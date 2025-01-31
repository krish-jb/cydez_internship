# Python program to delete vowels in a given string.
string = "Hello, World!"
string = "".join([i for i in string if i.lower() not in ['a', 'e', 'i', 'o', 'u']])
print(string)
