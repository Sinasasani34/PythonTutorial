from car import ElectricCar

my_leaf = ElectricCar("nissan", "maxima", 2009)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()