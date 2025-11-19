favorite_language = {
    'sina': ['JavaScript', 'TypeScript', 'Python', 'Java'],
    'sara': ['GoLang', 'SQL'],
    "sevda": ['C++'],
    'hamid': ['python', 'C#'],
}

for name, languages in favorite_language.items():
    print(f"\n{name.title()}'s favorite language is: ")
    for language in languages:
        print(f'\t{language.title()}')
print('-------------------------------------------')
# prac
for name, languages in favorite_language.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite language is: ")
        for language in languages:
            print(f'\t{language.title()}')
    else:
        print(f"\n{name.title()}'s favorite language is: {languages[0].title()}")