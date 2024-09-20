# Lambda Expression - Functions that return a function

def multiply(a,b):
    return lambda a,b: a*b

answer = multiply(3,4)
print(answer(3,4))  
