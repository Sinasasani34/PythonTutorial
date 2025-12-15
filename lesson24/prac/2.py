# دریافت ورودی از کاربر

sandwich_orders = []

print("Enter sandwich orders (type 'done' when finished):")

while True:
    # متد strip برای حذف فاصله های اضافه هستش
    order = input("Sandwich name: ").strip().lower()
    if order == 'done':
        break
    sandwich_orders.append(order)

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
