import re

string = "00abbsfskf_ksdhksjd000"

a = re.search( r'[a-z]+_[a-z]*', string)
print(a[0] if a else 'Not found')