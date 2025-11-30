alien_0 = {'color': "Green", 'Point': 5}
alien_1 = {'color': "yellow", 'Point': 10}
alien_2 = {'color': "red", 'Point': 15}

aliens = []

for alien in range(30):
    new_alien = {'color': 'green', "point": 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
    # elif alien['color'] == 'yellow':
    #     alien['color'] = 'red'
    #     alien['speed'] = 'fast'
    #     alien['point'] = 15
        
for alien in aliens[:5]:
    print(alien)
print('...')
print(f"totla number of alien's {len(aliens)}")