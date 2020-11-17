from utils import names


def binary_search(list, key):
    """Returns the position of key in the list if found, "N/A" otherwise.

    List must be sorted.
    """

    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1

    return "N/A"


for name in names:
    binary_search(names, name)
