active = True

while active:
    topping = input("یک ماده پیتزا وارد کنید (برای خروج 'quit'): ")

    if topping == "quit":
        active = False
        print("برنامه متوقف شد.")
    else:
        print(f"{topping} به پیتزا اضافه شد!\n")
