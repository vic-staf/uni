import re

string = "00abbsfsFFFFkassnake  dhksjd00b0"
a = re.sub("_", " ", string).title().replace(" ", "")

print(a if a else 'Not found')