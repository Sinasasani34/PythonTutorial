trucks = ['scania', 'volvo', 'benz', 'leyland', 'renault', 'Iran-Khodro']
print('The first three items in the list are: ')
for res in trucks[0:3]:
    print("\t",res)

print('Three items from the middle of the list are: ')
for res in trucks[2:5]:
    print("\t",res)

print('The last three items of the list are: ')
for res in trucks[3:]:
    print("\t",res)

print('--------------------------')
my_pizza = ['pepperoni', 'pizza', 'mushroom', 'onion']
friend_pizza = my_pizza[:]
my_pizza.append('my mommies pizza')
friend_pizza.append('dada baba pizza')
print('My favorite pizza is: ')
for res in my_pizza:
    print("\t",res)
print('friend favorite pizza is: ')
for res in friend_pizza:
    print("\t",res)