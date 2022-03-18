import re

text = 'a'
patterns = r'\bab{2,3}\b'

if re.search(patterns, text):
    print("Yes found")
else:
    print("Not found")