# Assign a different name to function and call it through the new name
def add(x, y):
    return x + y


addition = add


print(addition(20, 30))