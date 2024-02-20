import re

string = "00abbsfsFFFFkasdhksjd00b0"

a = re.search( r'a(\S)*b', string)
print(a[0] if a else 'Not found')