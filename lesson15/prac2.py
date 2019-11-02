available_users = ['Sina', 'Mahsa', 'Hamid', 'Sevda', 'Admin']
request_user = ['Sina', 'Hamid']
if request_user:
    for req in request_user:
        if req in available_users:
            print(f"Hello {req} :)")
        else:
            print(f"Dear {req}, you are not authorized.")
else:
    print("We need to find some users!")
print('\nDone!')