import re

string = "00abbbbb00"

a = re.search( r'ab*', string)
print(a[0] if a else 'Not found')