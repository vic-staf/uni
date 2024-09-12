import string

def generate_files():
    for letter in string.ascii_uppercase:
        file_name = letter + ".txt"
        with open(file_name, "w") as file:
            file.write("This is the content of " + file_name)

generate_files()