def make_pizza(*toppings):
    print("\n making a pizza with the following toppings")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')