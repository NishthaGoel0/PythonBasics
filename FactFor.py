# factorial using for function

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    
num = int(input("Enter Any positive number:"))   
fact = factorial(num)
print("Factorial of",num,"is:",fact)


        