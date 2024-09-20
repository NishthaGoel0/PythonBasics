# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a,b, negative):
    if negative:
        if a<0 and b<0:
           return True
        return False
    else:
        if (a<0 and b>0) or (a>0 and b<0):
            return True
        return False

check = pos_neg(1, -1, False)
print(check)
check = pos_neg(-1, 1, False)
print(check)
check = pos_neg(-4, -5, True)
print(check)
check = pos_neg(-4, -5, False) 
print(check)