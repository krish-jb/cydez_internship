# Display all duplicate items from a list
data = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
duplicates = []
for i in data:
    if data.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
        print(i)
    