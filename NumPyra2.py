# Printing Numbers in a Simple Triangle Pattern
"""
1
22
333
4444
"""

n = int(input("Enter Any Number: "))
m=1
while n>=m:
    for i in range (0,m+1):
        print(m,end="")
        
    m +=1
    print("")
    