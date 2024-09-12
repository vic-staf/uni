import re

string = "PythonExercisesPracticeSolution"
a = re.sub(r"(\w)([A-Z])", r"\1 \2", string)

print(a if a else 'Not found')