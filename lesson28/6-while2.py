def get_formatted_name(firstname, lastname):
    fullname = f"{firstname} {lastname}"
    return fullname
# this is an infinity loop
while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break

    formattedName = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formattedName}")
    