import shelve

# fruit = shelve.open('ShelfTest)       # Remove indentation lines 5-9 and remove/comment line 4
with shelve.open('ShelfTest') as fruit:
    # fruit['orange'] = "a sweet, orange, citrus fruit"
    # fruit['apple'] = "good for making cider"
    # fruit['lemon'] = "a sour, yellow citrus fruit"
    # fruit['grape'] = "a small, sweet fruit growing in bunches"
    # fruit['lime'] = "a sour, green citrus fruit"

    # print(fruit["lemon"])
    # print(fruit["grape"])

    # fruit["lime"] = "great with tequila"

    # for snack in fruit:
    #     print(snack + ": " + fruit[snack])

    # while True:
    #     dict_key = input("Please enter a fruit: ")
    #     if dict_key == "quit":
    #         break
    #
    #     if dict_key in fruit:
    #         description = fruit[dict_key]
    #         print(description)
    #     else:
    #         print("We don't have a " + dict_key)

    # ordered_keys = list(fruit.keys())
    # ordered_keys.sort()
    # for key in ordered_keys:
    #     print(key + ": " + fruit[key])

    for v in fruit.values():
        print(v)

    print(fruit.values())

    for f in fruit.items():
        print(f)

    print(fruit.items())

# fruit.close()                         # Remove comment for line 3+ to work

# with shelve.open('ShelfTest') as fruit:
#     fruit = {"orange": "a sweet, orange, citrus fruit",
#              "apple": "good for making cider",
#              "lemon": "a sour, yellow citrus fruit",
#              "grape": "a small, sweet fruit growing in bunches",
#              "lime": "a sour, green citrus fruit"}

# print(fruit["lemon"])
# print(fruit["grape"])
