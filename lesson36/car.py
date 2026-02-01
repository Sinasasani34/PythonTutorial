class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        longname = f"{self.year} {self.make} {self.model}"
        return longname.title()
        
    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"this car has a {self.battery_size}-kwh battery")
    
    def get_range(self):
        """print a statement about the range this battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"this car can go about {range} miles on a full charge")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()