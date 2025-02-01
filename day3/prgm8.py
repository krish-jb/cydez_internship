# Display numbers divisible by 5 from a list

numbers = [i for i in range(1, 101)]
for i in numbers:
    if i % 5 == 0:
        print(i, end=" ")
