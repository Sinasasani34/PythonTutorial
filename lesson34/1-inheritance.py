# we have tow type of classes
# Parent class
# child class

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
    
    def update_odometer(self, mileage):
        # mileage = kilometer
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer! ")

# use inheritance
class ElectricCar(Car):
    def __init__(self, make, model, year):
        # make connection between parent class and child class (super function)
        super().__init__(make, model, year)
        

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())