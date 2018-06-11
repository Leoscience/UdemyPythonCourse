fruit = {"orange": "a sweet, orange, citus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
# "apple": "round and crunchy"}  # Last entry remains

print(fruit)
# print(fruit["lemon"])

fruit["pear"] = "an odd shaped apple"
# print(fruit)
fruit["lime"] = "great with tequila"
# print(fruit)
# del fruit["lemon"]  # Only deletes the "lemon" entry
# del fruit  # Deletes all the dictionary
# fruit.clear() # Different from del - Dictionary remains, but empty
# print(fruit)
# print(fruit["tomato"])  # No "tomato" key -> error

# print(fruit)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We don't have a " + dict_key + ".")

# print(fruit)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     print(description)

# for snack in fruit:
#     print(fruit[snack])

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('-' * 40)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])
# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

# for val in fruit.values():
#     print(val)
#
# print('-' * 40)
#
# for key in fruit:
#     print(fruit[key])
fruit_keys = fruit.keys()
print(fruit_keys)
fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)
