from name_function import get_formmated_name

print("Enter 'q' to close the application! ")

while True:
    first = input("\nPlease enter your first name: ")
    if first == 'q':
        break
    last = input("\nPlease enter your last name: ")
    if last == 'q':
        break
    formmated_name = get_formmated_name(first, last)
    print(f"\tNeatly formmated name: {formmated_name}")