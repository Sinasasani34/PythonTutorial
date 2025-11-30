question = input("How many guests are you? ")
question = int(question)
if question >= 8:
    print("\nYou must wait for one more table")
else:
    print('\n your table is ready')