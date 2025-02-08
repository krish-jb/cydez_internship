from collections import defaultdict

my_dict = {
    "a": "",
    "b": "",
}

my_dict = defaultdict(lambda: 0)
print(my_dict['a'])