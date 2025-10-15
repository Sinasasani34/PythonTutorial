# Delete last index of array
truck = ['Scania','Volvo', 'IranKhodro','Benz', 'Daf']
print(truck)
# popped_truck = truck.pop(2)
print(truck)

last_owned_truck = truck.pop(4)
print(f"The last truck i owned was a {last_owned_truck.title()}")
first_owned_truck = truck.pop(0)
print(f"The first truck i owned was a {first_owned_truck.title()}")