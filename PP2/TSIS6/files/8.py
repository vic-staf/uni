import os

def delete(path):
    if os.path.exists(path): 
        if os.access(path, os.X_OK): os.remove(path)
        else : print("file does not executable ")
    else: print("file does not exist")

path = r"D:\Desktop\uni\TSIS6\files\example.txt"
delete(path)