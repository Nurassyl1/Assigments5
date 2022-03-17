import re

text = 'a'
patterns = r'\ba(b*)\b'

if re.search(patterns, text):
    print("Yes found")
else:
    print("Not found")