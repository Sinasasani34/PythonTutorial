from pathlib import Path

path = Path(r'e:\PythonCourseCode\lesson39\pi-digit.txt')
contents = path.read_text()
lines = contents.splitlines()
# return lines in array
print(lines)

for line in lines:
    print(lines)