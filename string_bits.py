# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
  str1 = ""
  for i in range(len(str)):
    if i % 2 == 0:
      str1 = str1 + str[i]
    else:
      continue
  return str1
  
x = string_bits('Chocoate')
print(x)
x = string_bits('pi')
print(x)