import re
texto= input()
print (re.search("Hola", texto))


import re
texto = input()
print(re.findall("[a-z]*er", texto))