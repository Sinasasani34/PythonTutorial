print("Give me tow numbers to divide them")
print("Enter 'q' to exit program")

while True:
    first_number = input("\nEnter first number: ")
    if first_number == "q":
        break
    second_number = input("\nEnter second number: ")
    if second_number == "q":
        break
    
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cant divide to 0! ")
    else:
        print(answer)
        