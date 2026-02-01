from pathlib import Path

contents = "I love Programming. \n"
contents += "I love to creating new games. \n"
contents += "I also love working with data. \n"

path = Path('programming.txt')
path.write_text(contents)