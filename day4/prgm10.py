# Remove items from a list while iterating
data = [1, 2, 3, 4, 5]

for i in data:
    if i == 3:
        data.remove(i)
        
print(data)