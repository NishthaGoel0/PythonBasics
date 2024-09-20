""" Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
Extras:
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

num = int(input("Enter Any Number to check: "))
if num % 4 == 0:
    print("Number is a multiple of 4")
elif num % 2 == 0:
    print(num, "is Even number")
else:
    print(num, "is Odd number")

check = int(input("give me a number to divide by: "))
if check != 0:
    if num % check == 0:
        print(num,"divides evenly by", check)
    else:
        print(num,"does not divides evenly by", check)
        print("Remainder is", num/check)
else:
    print("Wrong base number to divide by")