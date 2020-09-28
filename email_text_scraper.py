import re

text = 'A random string'
email = 'good morning missfitness_42@hotmail.com is my email address'

pattern = re.compile("\S+@\S+[.]\S+")

result = pattern.search(email)

print(result)
