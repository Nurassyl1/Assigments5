import re

text = 'test abb a0asd asd_asd abbb te21_22sfds ab asd abbbb abb_'

x = re.findall(r'\b[a-z]+_[a-z]+\b', text)
print(x)