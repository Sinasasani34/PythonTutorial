favorite_language = {
    'Sina': 'JavaScript',
    'Hamid': 'Python',
    'Mohammad': 'C',
    'Amir': 'Rust'
}

print('The following languages have been mentioned => ')
for lang in favorite_language.values():
    print(lang.title())