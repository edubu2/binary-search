from utils import names


def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return "N/A"


print(len(names))

for name in names:
    linear_search(names, name)
