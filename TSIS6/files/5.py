list = ["asd", "fgh", "tyy"]

with open(r"D:\Desktop\uni\TSIS6\files\file.txt", "w") as file:
    file.writelines(list)

with open(r"D:\Desktop\uni\TSIS6\files\file.txt", "r") as file:
    print(*file)