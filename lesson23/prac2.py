# ticket

message = "Enter your age (press 'quit' to exit program) => "

while True:
    age_input = input(message)

    if age_input.lower() == 'quit':
        print("Have good time.")
        break

    # convert input to number
    age = int(age_input)

    # check ticket
    if age < 3:
        print('ticket is free for you babe.\n')
    elif 3 <= age <= 12:
        print("its $10\n")
    else:
        print("its $15")