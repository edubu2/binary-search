"""Creates a list of first names, removes duplicates, and sorts it.
"""

with open("names.txt", "r") as names_file:
    names = []
    for line in names_file:
        names.append(line.strip("\n"))

names = set(names)
names = list(names)
names.sort()

