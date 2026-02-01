from pathlib import Path

# Rout of folder 
p = Path(r"e:\PythonCourseCode\lesson38\pi-digit.txt")
contents = p.read_text()
print(contents)