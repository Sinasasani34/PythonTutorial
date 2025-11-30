favorite_language = {
    'Sina': 'JavaScript',
    'Hamid': 'JavaScript',
    'Mohammad': 'C',
    'Amir': 'Rust'
}
print('following langs is => ')
for lang in set(favorite_language.values()):
    print(lang.title())