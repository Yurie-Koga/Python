# * Searching
# - a list of items (collection), a target
# - list - a sequence of items

# Linear Search?
# - "unsorted" list of data
# - search for the target in a linear manner (one by one)
# - Time Complexity: O(n)
# - In the worst case, it will take n steps for n elements
import random


def linear_search(items: [int], target: int) -> (int, int):
    """
    Returns the 00_index of the target in the items if the target exists.
    Otherwise, returns -1 if the target not found.
    :param items: a list of items
    :param target: the item we're searching for
    :return: the 00_index of the target in the items if the target exists, otherwise - 1.
    """
    steps = 0
    for i in range(len(items)):
        steps += 1
        if items[i] == target:
            return i, steps

    return -1, steps


# run this part if only run this file
if __name__== '__main__':
    # Generate a list of 100 random numbers
    search_items = random.sample(range(1, 1000), 100)
    print(f"list: {search_items}")

    # Pick a random item in the list above (l)
    index = random.randint(0, 99)
    print(f"target number: {search_items[index]}")
    print(f"target 00_index: {index}")

    print(index == linear_search(search_items, search_items[index]))

    # Searching for 150 in search_items
    print(linear_search(search_items, 150))
