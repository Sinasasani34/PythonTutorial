def build_person(firstname, lastname):
    person = {
        'firstname': firstname,
        'last': lastname
    }
    return person
name = build_person("Sina", "Sasani")
print(name)