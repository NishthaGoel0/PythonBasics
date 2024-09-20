#Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

def not_string(str):
    # Slice the string to extract first 3 characters
    str1 = str[0:3]
    #print(str1)
    if str1 != "not":
        return "not " +str"
    else:
        return str
        
result = not_string('candy')
print(result)
result = not_string('not bad')
print(result)
result = not_string('not')
print(result)