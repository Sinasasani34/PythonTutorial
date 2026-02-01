from pathlib import Path

path = Path(r"e:\PythonCourseCode\lesson41\pi_digit.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""

for line in lines:
    pi_string += line

# show 50 chars of pi digit
print(f"{pi_string[:52]}...")
print(len(pi_string))