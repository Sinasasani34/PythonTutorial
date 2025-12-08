# برای برنامه ای که تنها هنگامی اجرا میشود که شرط های زیادی صحیح باشد، میتوان یک متغیر تعریف کرد که تا فعال بودن یا فعال نبودن برنامه را تعیین میکند .
# این متغیر flg نامیده میشود. 
prompt = "\nTell me something, and i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)