import re

string = "00abbsfsAFFFFkaasAsnake A dhksjd00b0"
a = re.split(r'([A-Z])', string)

print(a if a else 'Not found')

