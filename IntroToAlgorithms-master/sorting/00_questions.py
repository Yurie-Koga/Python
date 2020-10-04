#Bubble Sort - "Bubbling" the largest element to the right!
# (pseudo-code): step-by-step written outline of your code
# list = [...]
# for each i from 1 to len(list)
#     compare two adjacent elements
#     if the first element is greater than the second element
#         swap two elements

# Time Complexity
# O(n^2) algorithm



def bubble_sort(alist):
    pass


def bubble_sort_mine(items: [int]):
    pass

def bubble_sort_mine2(items: [int]):
    pass

def bubble_sort_teacher(items: [int]):
    pass

def bubble_sort_teacher_improved(items: [int]):
    pass


# Selection Sort
# (pseudo-code)
# for each scan from 0 to len(alist)
#     find the min element (linear search)  : If I use binary search here, could be faster? let's check later
#     swap the min element with alist[scan]

# Time Complexity
# O(n^2) algorithm

import random

def selection_sort_original(alist):
    pass

def selection_sort_(items: [int]):
    pass

def selection_sort_improved(items: [int]):

    pass


if __name__== '__main__':
    print("---------- Bubble Sort ----------")
    # Bubble Sort
    a = [5, 1, 3, 2, 4]
    # bubble_sort(a)
    # print(a)
    b = [5, 1, 3, 2, 4]
    # bubble_sort_mine(b)
    # print(b)

    # test
    alist = random.sample(range(1, 500), 300)
    alist_copy = alist[:]
    # alist = [6, 5, 4, 3, 2, 1, 89, 45, 23, 12]
    # blist = [6, 5, 4, 3, 2, 1, 89, 45, 23, 12]
    b = alist[:]
    b2 = alist[:]
    bubble_sort_mine(b)
    print(b)
    bubble_sort_mine2(b2)
    print(b2)

    bubble_sort_teacher(alist)
    bubble_sort_teacher_improved(alist_copy)

    print("---------- Selection Sort ----------")
    # Selection Sort
    a = [5, 1, 4, 2, 3]
    #selection_sort_original(a)
    selection_sort_(a)
    print(a)

    # test
    alist = random.sample(range(1, 500), 300)
    alist_copy = alist[:]
    selection_sort_(alist)
    selection_sort_improved(alist_copy)
    print(alist)