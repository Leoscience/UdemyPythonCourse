# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))

# parrot_list = ["non pinin'", "no more", "a stiff", "bereft of live"]
#
# parrot_list.append("A Norwegian Blue")
#
# for state in parrot_list:
#     print("This parrot is " + state)
#
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
# numbers_in_order = sorted(numbers)
#
# print(numbers_in_order)
#
# if numbers == numbers_in_order:
#     print("The lists are equal")
# else:
#     print("The lists are not equal")
#
# if numbers_in_order == sorted(numbers):
#     print("The lists are equal")
# else:
#     print("The lists are not equal")

# list_1 = []
# list_2 = list()
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal")
# else:
#     print("The lists are not equal")
#
# print(list("The lists are equal"))

# even = [2, 4, 6, 8]
#
# another_even = list(even)
# # another_even = sorted(even, reverse=True)
#
# print(another_even is even)  # Same variable in memory
# print(another_even == even)  # Same value
#
# another_even.sort(reverse=True)
# print(even)

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = [even, odd]
# print(numbers)
#
# for numbers_set in numbers:
#     print(numbers_set)
#
#     for value in numbers_set:
#         print(value)

# CHALLENGE
# add to the program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal.
# You will need to set up the menu as did in lines 71-79

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

# print(menu)

for meal in menu:
    if "spam" not in meal:
        for ingredient in meal:
            print(ingredient)
