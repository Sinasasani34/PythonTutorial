class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")
        
my_new_car = Car("Quik", 'plus', '1404')
print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# change value of attribute
my_new_car.odometer_reading = 120
my_new_car.read_odometer()