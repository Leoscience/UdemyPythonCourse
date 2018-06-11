# t = "a", "b", "c"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))

# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company" "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# # imelda = "More Mayhem", "Imilda May", 2011, (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
# imelda = "More Mayhem", "Imelda May", 2011, 1, "Pulling the Rug", 2, "Psycho", 3, "Mayhem", 4, "Kentish Town Waltz"
#
# print(imelda)
#
# title, artist, year, track1, track2, track3, track4 = imelda
# print(title)
# print(artist)
# print(year)
# print(track1)
# print(track2)
# print(track3)
# print(track4)

# metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# # metallica[0] = "Master of Puppets"  # Error, tuples does not support item assignment, but slicing and indexing...
#
# imelda = imelda[0], "Imelda May", imelda[2]
# print(imelda)

# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# print(metallica2)

# a = b = c = d = 12
# print(c)
# a, b = 12, 13
# print(a, b)
#
# a, b = b, a
# print("a is {}".format(a))
# print("b is {}".format(b))

# title, artist, year = imelda
# metallica2.append("Rock")  # If tuple is used, can't append / immutable => Less errors
# imelda.append("Jazz")

# title, artist, year = metallica2  # Error, too many values to unpack
# print(title)
# print(artist)
# print(year)

# CHALLENGE
# Given the tuple below that represents the Imleda May track "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma)

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"),
)
album, author, year, tracks = imelda
print("Album\t\tAuthor\t\tYear")
print(album, author, year, sep="\t")

for track in tracks:
    print("\t", track)

imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")]
)

print(imelda)

imelda[3].append((5, "All For You"))

title, artist, year, tracks = imelda
tracks.append((6, "Eternity"))
print(title)
print(artist)
print(year)
for song in tracks:
    track, title = song
    print("\tTrack number {}, Ttitle: {}".format(track, title))
