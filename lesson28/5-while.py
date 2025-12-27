def get_formatted_name(firstname, lastname):
    fullname = f"{firstname} {lastname}"
    return fullname
# this is an infinity loop
while True:
    print("\nPlease tell me your name: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formattedName = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formattedName}")