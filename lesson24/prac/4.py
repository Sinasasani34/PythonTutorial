responses = {}
polling_active = True

print("If you could visit one place in the world, where would you go?\n")

while polling_active:
    name = input("What's your name? ")
    place = input("Dream vacation place: ")

    responses[name] = place

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name} would like to visit {place}.")
