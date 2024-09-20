#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Extras: Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 

import datetime
name = input("Enter Your Name: ")
age = int(input("Enter Age: "))


def year(name,age):
    
    currentYear = datetime.date.today().year
    print(f"Current Year {currentYear}")
    
    if age >= 100:
        print("Wow you already reached centuary")
        
    else:
        num = int(input("Repeat: "))
        year_of_100 = currentYear + (100 - age)
        while num > 0:
            print(name + " will turn 100 years old in year " + str(year_of_100))
            num -=1
    
year(name,age)  