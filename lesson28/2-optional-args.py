# اختیاری کردن کردن آرگومان
# def get_formatted_name(firstname, middlename, lastname):
#     """Return a full name, neatly formatted"""
#     fullname = f"{firstname} {middlename} {lastname}"
#     return fullname.title()

# name = get_formatted_name("A", "sina", "sasani")
# print(name)

# optional item
def get_formatted_name(firstname, lastname, middlename = ''):
    """Return a full name, neatly formatted"""
    # use the middlename argument optional
    if middlename:
        fullname = f"{firstname} {middlename} {lastname}"
    else:
        fullname = f"{firstname} {lastname}"
    return fullname.title()
name = get_formatted_name("sina", "sasani")
print(name)