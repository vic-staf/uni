import re

string = "00abbsfsFFFFksdhksjd000"

a = re.search( r'[A-Z][a-z]+', string)
print(a[0] if a else 'Not found')