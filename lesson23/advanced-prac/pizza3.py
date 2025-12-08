while True:
    topping = input("یک ماده پیتزا وارد کنید (برای خروج 'quit'): ")

    if topping == "quit":
        print("خروج از برنامه...")
        break

    print(f"{topping} به پیتزا اضافه شد!\n")
