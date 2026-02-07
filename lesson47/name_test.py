from name_function import get_formmated_name

# python -m pytest 
# run in terminal
def test_first_last_name():
    formatted_name = get_formmated_name("sina", "sasani")
    assert formatted_name == "Sina Sasani"
# این بخش در خروجی نمایش میدهد که این تابع به درستی دارد کار میکند و مشکلی ندارد.