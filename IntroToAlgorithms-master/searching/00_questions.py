import random

# Binary Search
# - "sorted" list of data
# - Keep comparing the middle item in the list to the target
#   while removing the half of the list from the search range.
# - Time Complexity: O(lg N)


def binary_search_iterative(items: [str], target: str) -> (int, int):
    """
    Returns the 00_index of the target in the items if the target exists.
    Otherwise, returns -1 if the target not found.
    Using binary search algorithm
    Time Complexity O(lg N)
    :param items: a list of items
    :param target: the item we're searching for
    :return: the 00_index of the target in the items if the target exists, otherwise - 1.
    """

    pass

def binary_search_recursive(items: [str], target: str) -> (int, int):
    """
    Returns the 00_index of the target in the items if the target exists.
    Otherwise, returns -1 if the target not found.
    Using binary search algorithm
    Time Complexity O(lg N)
    :param items: a list of items
    :param target: the item we're searching for
    :return: the 00_index of the target in the items if the target exists, otherwise - 1.
    """

    pass


# * Searching
# - a list of items (collection), a target
# - list - a sequence of items

# Linear Search?
# - "unsorted" list of data
# - search for the target in a linear manner (one by one)
# - Time Complexity: O(n)
# - In the worst case, it will take n steps for n elements


def linear_search(items: [int], target: int) -> (int, int):
    """
    Returns the 00_index of the target in the items if the target exists.
    Otherwise, returns -1 if the target not found.
    :param items: a list of items
    :param target: the item we're searching for
    :return: the 00_index of the target in the items if the target exists, otherwise - 1.
    """
    pass


if __name__== '__main__':
    print("-------- Binary Search --------")
    countries = ["Australia", "Brazil", "Canada", "Denmark", "Ecuador",
                "France", "Germany", "Honduras", "Italy", "Japan",
                "Korea", "Latvia", "Malaysia", "Norway", "Oman", "Poland",
                "Qatar", "Russia", "Spain", "Thailand", "USA", "Vietnam",
                "Wales", "Yemen", "Zambia"]

    # lg 26 -> 4.xxx
    target = "Italy"
    pos, steps = binary_search_iterative(countries, target)
    print(f"Found {target} at {pos} 00_index in {steps} steps")

    target = "Italy"
    pos, steps = binary_search_recursive(countries, target)
    print(f"Found {target} at {pos} 00_index in {steps} steps")


    print("-------- Linear Search --------")
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