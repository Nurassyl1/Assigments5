import re

text = 'test abb a0asd Aasdas AasdA AasdaZsa Aasda2 ASDsadas Almaty asd_asd abbb te21_22sfds ab asd abbbb abb_'

x = re.findall(r'\b[A-Z][a-z]+\b', text)
print(x)