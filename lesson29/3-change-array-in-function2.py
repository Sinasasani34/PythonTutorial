# شرکتی را در نظر بگیرید که مدل های چاپ شده سه بعدی از ایده های طراحی شده به وسیله کاربران را تولید میکند.
# طرح هایی که باید چاپ شوند، در یک فهرست ذخیره میشوند و پس از چاپ، به یک فهرست جداگانه منتقل میشوند
# using function
def print_models(unprinted_designs, complited_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        complited_models.append(current_design)
def show_complited_models(complited_models):
    print("\nthe following models have been printed: ")
    for complited_model in complited_models:
        print(complited_model)
unprinted_designs = ['phone case', 'robot pendant', 'nazi germany logo']
complited_models = []
# print_models(unprinted_designs, complited_models)
# پیشگیری از تغییر یک فهرست و آرایه
print_models(unprinted_designs[:], complited_models)
show_complited_models(complited_models)