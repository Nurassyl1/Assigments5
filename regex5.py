import re

text = 'test abb a0asd Aasdas AasdAb AasdaZsa Aasda2 ASDs1_22sfds ab asd abbbb abb_ asfdgfrsegfb'

x = re.findall(r'a\w+b\b', text)
print(x)