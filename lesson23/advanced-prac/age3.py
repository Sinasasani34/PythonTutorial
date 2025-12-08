while True:
    age_input = input("سن خود را وارد کنید (برای خروج 'quit' را وارد کنید): ")

    if age_input == "quit":
        print("خروج از برنامه...")
        break

    age = int(age_input)
    if age < 3:
        print("بلیط برای شما رایگان است.\n")
    elif 3 <= age <= 12:
        print("قیمت بلیط 10 دلار است.\n")
    else:
        print("قیمت بلیط 15 دلار است.\n")