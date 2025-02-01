# Define a function that accepts 2 values and return its sum, subtraction and multiplication.


def aop(num1, num2):
    return {"sum": num1 + num2, "difference": num1 - num2, "product": num1 * num2}


result = aop(20, 10)
print(result)
