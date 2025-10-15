motor = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motor)

# motor.remove('ducati')
print(motor)
# remove with reason
too_expensive = 'ducati'
motor.remove(too_expensive)
print(motor)
# its not removed from the list. remove function gives you access to see the removed value
print(f"\nA {too_expensive.title()} is too expensive for me.")