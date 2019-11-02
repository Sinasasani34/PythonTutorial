favorite_language = {
    'Sina': 'JavaScript',
    'Hamid': 'Python',
    'Mohammad': 'C',
    'Amir': 'Rust'
}
friends = ['Hamid', 'Mohammad']
for name in favorite_language.keys():
    print(f'He {name.title()}')
    
    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you love {language}!")