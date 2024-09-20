# Printing Numbers Using Inverted Pyramids
"""
111111
22222
3333
444
55
6
"""
n = int(input("Enter Any Number: "))
m = 0

for index in range(n,0,-1):
    m +=1
    for n in range(1,index+1):
        print(m,end=' ')
        
    print("")
    