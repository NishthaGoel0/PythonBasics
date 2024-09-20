#Printing the Same Digit Pattern Using Inverted Pyramid

n = int(input("Enter Any Number: "))
m = n
while m>0:
    for index in range(m,0,-1):
        print(n,end=' ')
    m -=1    
    print("")