# Create a function with variable length of arguments

def to_csv(*a):
    for i in range(len(a)):
        print(a[i], end="," if i != len(a) - 1 else "")

to_csv(1, 2, 3, 4, 5, 6, 7)
