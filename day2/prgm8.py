'''
Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
    
        Cost price (in Rs)                                       Tax
        > 100000                                                  15%
        > 50000 and <= 100000                                     10%
        <= 50000                                                  5%

'''
cost_price = int(input("Enter cost price of bike(₹): "))
tax = 0
if cost_price > 100000:
    tax = cost_price * 0.15
elif cost_price > 50000:
    tax = cost_price * 0.1
else:
    tax = cost_price * 0.05

print(f"Tax = {tax}")

