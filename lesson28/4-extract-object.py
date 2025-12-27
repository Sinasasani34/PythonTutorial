def build_person(firstname, lastname, age = ''):
    person = {
        'firstname': firstname,
        'last': lastname
    }
    if age:
        person['age'] = age
    return person
name = build_person("Sina", "Sasani", age=21)
print(name)