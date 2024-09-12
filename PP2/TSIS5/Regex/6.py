import re

string = "00abbsfsFFFFkas  dhksjd00b0"
a = re.sub("[ ,.]", ":", string)

print(a if a else 'Not found')
