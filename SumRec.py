#Sum of 1 to 100 using reculsive function
# Sum(n) = n+Sum(n-1)

def sum(n):
    if n>0:
        return n + sum(n-1)
    return 0

num =int(input("Enter any positive Number:"))    
result = sum(100)
print("Sum of 1 to 100 numbers is:",result)