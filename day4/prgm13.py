'''
Print the following number pattern
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
'''

n = 5
for i in range(1, n + 1):
    print(str(i) * (n - i + 1))
