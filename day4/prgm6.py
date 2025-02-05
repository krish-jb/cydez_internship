# Delete a list of keys from a dictionary
greetings = {
    "Hello": 1,
    "Bonjour": 2,
    "Konichiwa": 3,
    "Ni hai": 4
}
to_remove = ["Hello", "Bonjour"]


items = {key: value for key, value in greetings.items() if key not in to_remove}
print(items)
