# pizza topping
message = "Enter your own topping for your pizza (Press 'quit' to exit) => "

while True:
    topping = input(message)
    if topping.lower() == "quit":
        print("Have a good time <3")
        break
    print(f"{topping} has added to your pizza")