# sandwich list
sandwich_orders = ['tuna', 'chicken', 'beef', 'vegetable', 'cheese']

# finished sandwiches
finished_sandwiches = []

# process orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made yor {current_sandwich}")

    finished_sandwiches.append(current_sandwich)
print("\nAll sandwiches have been made: ")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")