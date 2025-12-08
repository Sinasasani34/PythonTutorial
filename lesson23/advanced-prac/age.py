age = ""
message = "Enter your age "
message += "(For exit program enter 'quit' . ) => "
while age != 'quit':
    age = input(message)

    if age == "quit":
        print('Program has been done')
    else:
        age = int(age)
        if age < 3:
            print("Ticket is free for you\n")
        elif 3 <= age <= 12:
            print("Ticket is $10\n")
        else:
            print('ticket is $15\n')

