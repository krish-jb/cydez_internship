# Accept the age of 4 people and display the youngest one?

ages = []
for i in range(4):
    ages.append(int(input(f"Enter the age of person {i + 1}: ")))
ages.sort()
print(f"The youngest is {ages[0]} years old!")
