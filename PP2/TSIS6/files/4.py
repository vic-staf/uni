import os

file = open(r"D:\Desktop\uni\TSIS6\files\file.txt", "r")
count = 0
for i in file:
        count+= 1
print(count)