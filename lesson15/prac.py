users = ['Sina', 'Mahsa', 'Hamid', 'Sevda', 'Admin']

for user in users:
    if user == 'Admin':
        print(f"Hello Dear {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, welcome to our website!")