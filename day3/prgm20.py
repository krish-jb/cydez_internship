# Write a Python program to select a random element from a list, set, dictionary (value), and a file from a directory. Use random.choice()
from random import choice
from os import scandir

_list = [i for i in range(1, 11)]
_set = set(_list)
_dict = {str(i - 1): i for i in _set}
files = [f.name for f in scandir() if f.is_file()]

print(choice(_list))
print(choice(tuple(_set)))
print(choice(tuple(_dict.values())))
print(choice(files))
