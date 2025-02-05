# Convert two lists into a dictionary

keys_ = ["One", "Two", "Three"]
values_ = [1, 2, 3]

result = {key: val for key, val in zip(keys_, values_)}
print(result)