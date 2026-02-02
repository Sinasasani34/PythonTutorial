from pathlib import Path
import json

username = input("Whats your name? ")

path = Path("username.json")
contents = json.dumps(username)
path.write_text(contents)

print(f"we'll remember you when you come back, {username}! ")