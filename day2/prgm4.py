''' Write a Python program to construct the following pattern, using a nested for loop.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''

n = 5

for i in range(1, n + 1):
    print("* " * i)

for i in range(n - 1, 0, -1):
    print("* " * i)
