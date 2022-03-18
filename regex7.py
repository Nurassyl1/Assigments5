import re

text = 'Hello_My_World'

x = re.sub('_', '', text)
print(x)