# Reculsive Function - The function which keeps calling itself until the condition to call it fails...You need to use condition or it can go infinite iteration

def count_down(start):
    """ Count down from a number  """
    print(start)

    # call the count_down if the next
    # number is greater than 0
    next = start - 1
    if next > 0:
        count_down(next)

num = int(input("Enter a positive number: "))
count_down(num)