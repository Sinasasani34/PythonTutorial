my_trucks = ['scania', 'benz', 'volvo']
# هر عنصر جدا نگهداری میشود یعنی مای تراک یک عنصر جدا از عنصر فرند تراکس هستش که در خط های بعدی اینو ثابت میکنیم
friend_trucks = my_trucks[:]
print('my favourite trucks: ')
print(my_trucks)

print('\n My friends favourite trucks: ')
print(friend_trucks)

# ثابت کردن جدا بودن مقادیر هر لیست(مای تراک، فرند تراک)
my_trucks.append('benz-Axor')
friend_trucks.append('Iran-Khodro')
print('my favourite trucks: ')
print(my_trucks)

print('\n My friends favourite trucks: ')
print(friend_trucks)