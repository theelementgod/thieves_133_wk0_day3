# age = 689

# if age > 64:
#     print('senior')
# elif age < 18:
#     print('kid')
# else:
#     print('adult')

def voter_age(num):
    if age > 64:
        print('senior')
    elif age < 18:
        print('kid')
    else:
        print('adult')

        # voter_age(13)
        # voter_age(45)
        # voter_age(78)

names = ['daniel', 'stephen', 'gianni', 'marina', 'heather']

names2 = names[:]
print(names, names2)
names.append('brandt')
names2.append('Lee')
print(names, names2)


# def list_name():
#     for name in names:
#         last = input('What is your last name?     ')
#         print(name.title() + " " + last.title())

# # list_name()

# def namer():
#     n_list = []
#     while True:
#         menu = input('add name?   y/n  ')
#         if menu != 'n':
#             name = input('what is your name?')
#             n_list.append(name.title())
#         else:
#             break
#     for i in range(len(n_list)):
#         print(f"{i+1}- {n_list[i]}")

# namer()






