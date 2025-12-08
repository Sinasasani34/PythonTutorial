topping = ""

while topping != "quit":
    topping = input("یک ماده پیتزا وارد کنید (برای خروج 'quit'): ")

    if topping != "quit":
        print(f"{topping} به پیتزا اضافه شد!\n")
    else:
        print("برنامه پایان یافت.")