# شرکتی را در نظر بگیرید که مدل های چاپ شده سه بعدی از ایده های طراحی شده به وسیله کاربران را تولید میکند.
# طرح هایی که باید چاپ شوند، در یک فهرست ذخیره میشوند و پس از چاپ، به یک فهرست جداگانه منتقل میشوند
# روش بدون تابع
# Start with some designs that need to be printed
unprinted_design = ['phone case', 'robot pendant', 'nazi germany logo']
complited_models = []

# simulate printing each design, until none are left
# Move each design to complited_models after printing
while unprinted_design:
    current_design = unprinted_design.pop()
    print(f"Printing model: {current_design}")
    complited_models.append(current_design)
print("\nthe following models have been printed: ")
for complited_model in complited_models:
    print(complited_model)
