class Strings:
    def __init__(self):
        self.string = ""

    def print_string(self):
        return self.string.upper()

    def get_string(self):
        self.string = input("Enter a word: ")
        return self.string


t = Strings()
print(t.get_string())
print(t.print_string())