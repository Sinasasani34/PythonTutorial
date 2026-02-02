from pathlib import Path

def count_words(filename): 
    try:
        contents = filename.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words")
    

filenames = ['text.txt', 'app.js', 'main.ts']

for fn in filenames:
    path = Path(fn)
    count_words(path)