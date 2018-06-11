# string = "1234567890"

# for char in string:
#     print(char)

# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
#
# # print(next(my_iterator))  # Error StopIteration

# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)

# CHALLENGE
# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using iter() function.
#
# Use a for loop to loop 'n' times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item
#
# hint: use the len() function rather than counting the number if items in the list.

list_1 = ["air", "blender", "conquer", "dragon", "elegant", "fire"]
list_iterator = iter(list_1)

for i in range(0, len(list_1)):
    print(next(list_iterator))
