# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

vowels = {"a", "e", "i", "o", "u"}
# vowels = frozenset("aeiou")

text = input("Please enter a text: ")
text_set = set(text)
print(sorted(text_set - vowels))
