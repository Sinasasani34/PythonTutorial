request_toppings = []

if request_toppings:
    for request in request_toppings:
        print(f'Adding {request}')
    print('\n Finished making your pizza!')
else:
    print('Are you sure you want plain pizza?')