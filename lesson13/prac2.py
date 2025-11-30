car = 'Toyota'
color = 'red'
age = 18
city = 'tehran'
number = 10

print(car.lower() == 'toyota')
print(age < 18)
print(age > 18)
print(age <= 18)
print(age >= 18)
print(age == 18)
print(age != 18)

print(age >= 18 and number > 10)
print(age >= 18 or number > 10)

print('Benz' in car)
benz = 'benz'
if benz not in car:
    print(f'{benz.title()} is not in the car category')