import re

string = "00abbb00"

a = re.search( r'ab{2,3}', string)
print(a[0] if a else 'Not found')