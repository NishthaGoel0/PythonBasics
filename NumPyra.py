# Number Pattern Semi-Pyramid
"""
1
1 2
1 2 3
"""
n = int(input("Enter Any Number: "))
m = 1
while n>= m:
    for index in range(1,m):
        print(index, end=" ")
    m +=1 
    print("")