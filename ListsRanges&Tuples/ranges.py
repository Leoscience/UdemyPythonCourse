# my_list = list(range(10))
# print(my_list)
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# print(even)
# print(odd)

# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index('e'))
# print(my_string[4])
#
# small_decimals = range(10)
# print(small_decimals)
#
# print(small_decimals.index(3))
#
# odd = range(1, 10000, 2)
# print(odd)
#
# print(odd[985])
#
# sevens = range(7, 1000000, 7)
# x = int(input("Please enter a positive number less than one million: "))
# if x in sevens:
#     print("{} is divisible by seven.".format(x))
#
# print(small_decimals)
#
# my_range = small_decimals[::2]
#
# print(my_range)
# print(my_range.index(4))

# decimals = range(100)
# print(decimals)
#
# my_range = decimals[3:40:3]
# print(my_range)
#
# for i in my_range:
#     print(i)
#
# print('=' * 40)
#
# for i in range(3, 40, 3):
#     print(i)
#
# print(my_range == range(3, 40, 3))

# decimals = range(100)
# my_range = decimals[3:40:3]
# print(my_range == range(3, 40, 3))
# print(range(0, 5, 2) == range(0, 6, 2))
# print(list(range(0, 5, 2)))
# print(list(range(0, 6, 2)))
#
# r = range(0, 100)
# print(r)
#
# for i in r[::-2]:
#     print(i)
#
# print('*' * 40)
#
# for i in range(99, 0, -2):
#     print(i)
#
# print('*' * 40)
# print(range(0, 100)[::-2] == range(99, 0, -2))
#
# for i in range(0, 100, -2):
#     print(i)

# backString = "egaugnal lufrewop yrev a si nohtyP"
# print(backString[::-1])
#
# r = range(10)
# for i in r[::-1]:
#     print(i)

# CHALLENGE
# Experiment with different ranges and slices to get a feel for how they work.
# Remember that you can print the range as well as iterating through it to print
# its values, to check that your ranges are what you expected.
# You may also want to include things like:
#
o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in p:
    print(i)

# and see if you can work out what will be printed before running the program. If you are unsure, use a
# for loop to print out the values of 'o' to see why 'p' returns what it does.
