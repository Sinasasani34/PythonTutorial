class Dog:
    """A simple attempt tp model a dog"""
    
    # constractors on python
    # پارامتر self در تمامی متد های کلاس توی  پایتون اجباری است و در تمام متد ها باید اولین پارامتر باشد
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name} is sitting now")
    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog("Rex", 6)
# for access to the attributes of class use variable name.attribute_name like = my_dog.name
print(f"My dog name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
print('--------------------------------')
my_dog.sit()
my_dog.roll_over()
