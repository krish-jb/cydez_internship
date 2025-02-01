# Write a Python function that checks whether a passed string is palindrome or not.
def is_palindrome(string):
    return string == string[::-1]

string = input("Enter a string: ")
print(f"{string} is {"" if is_palindrome(string) else "not "}a palindrome!", sep="")
