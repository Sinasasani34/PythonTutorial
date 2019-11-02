current_users = ['Sina', 'Mahsa', 'Hamid', 'Sevda', 'NoName']
new_users = ['Sina', 'Hamid', 'Mohammad', 'Mehdi', 'Ali']

for user in new_users:
    if user in current_users:
        print(f"⚠️ نام کاربری «{user}» قبلاً استفاده شده است.")
        new_name = input("لطفاً یک نام کاربری جدید وارد کنید: ")

        if new_name in current_users:
            print(f"❌ نام «{new_name}» هم قبلاً استفاده شده! عملیات لغو شد.\n")
        else:
            current_users.append(new_name)
            print(f"✅ نام کاربری جدید «{new_name}» با موفقیت ثبت شد.\n")

    else:
        print(f"✅ نام کاربری «{user}» آزاد است و ثبت می‌شود.\n")
        current_users.append(user)