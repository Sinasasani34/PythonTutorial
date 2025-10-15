guests = ['Mahsa', 'Sina', 'Hamid', 'Jenifer']
print(f'I want you {guests[0]}')

jenifer = 'Jenifer'
guests.remove(jenifer)
print(f"{jenifer.title()} dont want to party")
print(guests)

guests.insert(0, 'Mommy')
guests.insert(2, 'Dad')
print(guests)

guests.append('Anne')
print(guests)

guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
print(guests)