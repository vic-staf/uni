import os

def list_directories_files(path):
    directories = []
    files = []
    all_directories_files = []
    
    for i in os.listdir(path):
        i_path = os.path.join(path,i)
        if os.path.isdir(i_path) == True:
            directories.append(i)
            all_directories_files.append(i)
        else : 
            files.append(i)
            all_directories_files.append(i)
    print(directories)
    print(files)
    print(all_directories_files)


path = r"D:\\Desktop\\uni"
list_directories_files(path)