from pathlib import Path

path = Path(r"e:\PythonCourseCode\lesson41\pi_digit.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""

for line in lines:
    pi_string += line

# find brithday in pi
# brithday format yymmdd
brithday = input("Enter your brithday, in the format of yymmdd: ")

if brithday in pi_string:
    print("Your brithday appears in the first milion digits of pi")
else:
    print("Your brithday is not in first milion digits of pi")