prompt = "\nPlease enter the name of a city you have visited => "
prompt += "\n(Enter 'quit' whene you are finished.) "

# شکستن حلقه و خارج شدن از حلقه با break 
while True:
    city = input(prompt)

    if city == 'quit':
        break # حلقه تا زمانی که quit وارد نشود اجرا میشود 
    else:
        print(f"I'd love to go to {city.title()}")