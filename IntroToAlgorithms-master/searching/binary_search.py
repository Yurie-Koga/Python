# Binary Search
# - "sorted" list of data
# - Keep comparing the middle item in the list to the target
#   while removing the half of the list from the search range.
# - Time Complexity: O(lg N)


def binary_search(items: [str], target: str) -> (int, int):
    """
    Returns the 00_index of the target in the items if the target exists.
    Otherwise, returns -1 if the target not found.
    Using binary search algorithm
    Time Complexity O(lg N)
    :param items: a list of items
    :param target: the item we're searching for
    :return: the 00_index of the target in the items if the target exists, otherwise - 1.
    """
    lower = 0
    upper = len(items) - 1
    steps = 0
    while lower <= upper:
        mid = (lower + upper) // 2
        steps += 1
        if items[mid] == target:
            return mid, steps
        elif items[mid] < target:
            lower = mid + 1
        else:
            upper = mid - 1

    return -1, steps


def number_of_steps(n: int):
    """
    :param n: a number of elements
    :return : a number of steps
    """
    l = 0
    u = n - 1
    steps = 0
    while l <= u:
        steps += 1
        m = (l + u) // 2
        l = m + 1
    return steps


if __name__== '__main__':
    countries = ["Australia", "Brazil", "Canada", "Denmark", "Ecuador",
                "France", "Germany", "Honduras", "Italy", "Japan",
                "Korea", "Latvia", "Malaysia", "Norway", "Oman", "Poland",
                "Qatar", "Russia", "Spain", "Thailand", "USA", "Vietnam",
                "Wales", "Yemen", "Zambia"]

    # lg 26 -> 4.xxx
    target = "Italy"
    pos, steps = binary_search(countries, target)
    print(f"Found {target} at {pos} 00_index in {steps} steps")

    print(f"steps of 8: {number_of_steps(600)}")
    print(256*256*256)
    print(2**11-1)