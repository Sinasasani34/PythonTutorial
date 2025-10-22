# بررسی عدم وجود یک مقدار در یک فهرست
banned_users = ['sina', 'mahsa', 'david']
user = 'maria'
if user not in banned_users:
    print(f'Dear {user.title()}, you can post a response if you wish')