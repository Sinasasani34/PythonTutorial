# for counter in range(1, 21):
    # print(counter)

# for counter in range(1, 1000001):
    # print(counter)

# num = range(1000001)
# print(min(num))
# print(max(num))
# print(sum(num))
#
# odd_numbers = range(1, 21, 2)
# for oddNumbers in odd_numbers:
#     print(oddNumbers)

# multi_nums_of_3 = list(range(3, 31, 3))
# for num in multi_nums_of_3:
#     print(num)


# cubes = []
# for num in range(1, 11):
#     cube = num ** 3
#     cubes.append(cube)
# for cube in cubes:
#     print(cube)

cubes = []
for num in range(1, 11):
    cube = num ** 3 # num ^ 3 => 1^3=1, ... 10^3=1000
    cubes.append(cube)
for cube in cubes:
    print(cube)