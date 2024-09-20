#Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str,n):
    str1 = ""
    for i in range(len(str)):
        if i==n:
           continue
        else:
            str1 = str1 + str[i]
    #result = str1[0:]
    return str1
   
result = missing_char('Hi', 0)
print(result)

def missing_char1(str,n):
    front = str[0:n]
    back = str[n+1:]
    return front + back

result = missing_char1('kitten', 4)
print(result)
result = missing_char1('chocolate', 8)
print(result)