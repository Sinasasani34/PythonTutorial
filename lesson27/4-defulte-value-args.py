def describe_pet(pet_name, animal_type = 'dog'):
    """Display information"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}. ")
describe_pet(pet_name="rex")
describe_pet("rex")