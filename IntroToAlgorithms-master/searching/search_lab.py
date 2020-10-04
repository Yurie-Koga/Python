# creat a function

# how to import
#from searching.linear_search import *
#from searching.binary_search import *

import os
#print(os.getcwd())
#os.chdir('/searching/')
#print(os.getcwd())

def linear_search(items: [str], target: str) -> (int, int):
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

# this is same as with open as
#f = open("words")
#f.close()
#

#with open("/Users/ujisaori/Downloads/IntroToAlgorithms-master/searching/words") as f:
with open(os.path.dirname(__file__) + "/words") as f:
    lines = f.readlines()

    # strip off the newline character for each word in the list
    # "list comprehension" (syntax) - python specific
    # stripped = []
    # for line in lines:
    #     stripped.append(line.strip().lower())
    lines = [line.strip().lower() for line in lines]

    target = input("Search word: ").lower()
    li = linear_search(lines, target)
    bi = binary_search(lines, target)

    print(f"Linear Search: found at {li[0]}, took {li[1]} steps")
    print(f"Binary Search: found at {bi[0]}, took {bi[1]} steps")