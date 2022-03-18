import re

text = 'Asad, asdwe asdasd.'

x = re.sub('\s|\.|,', ':', text)
print(x)