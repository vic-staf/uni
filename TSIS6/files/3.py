import os

def fileanddir(path):
    directory = []
    files = []
    if os.path.exists(path):
        directory.append(path)
        for i in os.listdir(path):
            i_path = os.path.join(path, i)
            if os.path.isdir(i_path) == False:
                files.append(i)

    else : print("File does not exist")
    print(directory)
    print(files)

path = r"D:\\Desktop\\uni"
fileanddir(path)
