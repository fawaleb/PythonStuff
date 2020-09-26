import re

text = 'A random string'

pattern = re.compile('[a-z]+')

result = pattern.search(text)

print(result)
