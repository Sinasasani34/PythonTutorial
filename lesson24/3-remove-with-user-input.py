# پرکردن یک ابجکت به وسیله کاربر 
responses = {}
# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # prompt for the person's name and response
    name = input("\nWhats your name? ")
    response = input("which mountain wholde you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response
    # find out if anyone else is going to take the poll
    repeat = input("Whold you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active: False
# polling is complete. show the result
print("\n--- Poll Result ---")
for names, res in responses:
    print(f"{names} Whold you like to climb {res}.")