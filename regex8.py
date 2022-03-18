import re

text = 'Hello my World. You are the Best asd A'

x = re.findall('[A-Z][^A-Z]*', text)
print(x)