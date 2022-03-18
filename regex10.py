import re

text = 'HelloMyWorlCamelcamel'

x = re.sub(r'(\w)([A-Z])', r'\1_\2', text)
print(x)