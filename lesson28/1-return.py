# return a simple value in function
def get_formatted_name(first_name, last_name):
    """return a full name, neatly formatted"""
    fullName = f"{first_name} {last_name}"
    return fullName.title()
musician = get_formatted_name("parviz", "meshkatian")
print(musician)