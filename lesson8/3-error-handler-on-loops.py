# incorrect loop usage
cars = ['bmw', 'audi', 'toyota', 'subaru']
# for car in cars:
# print(car.title())

for car in cars:
    print(f'{car.title()}, that was a greate list')
    print(f'i cant wait for next cars of {car.title()}\n')
print('thank you everyone')