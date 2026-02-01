from pathlib import Path

path = Path(r"e:\PythonCourseCode\lesson40\pi-digit.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""

for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))