# Bubble Sort - "Bubbling" the largest element to the right!
# (pseudo-code): step-by-step written outline of your code
# list = [...]
# for each i from 1 to len(list)
#     compare two adjacent elements
#     if the first element is greater than the second element
#         swap two elements

# Time Complexity
# O(n^2) algorithm

import random

def bubble_sort(alist):
    steps = 0
    for scan in range(len(alist)):
        swapped = False
        for j in range(len(alist) - 1 - scan):
            steps += 1
            if alist[j] > alist[j+1]:
                # alist[j], alist[j+1] = alist[j+1], alist[j]
                swapped = True
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp

        if not swapped:
            break

    print("steps:", steps)


def bubble_sort_mine(items: [int]):
    count = 0
    for scan in range(len(items) - 1):
        for i in range(len(items) - 1 - scan):
            count += 1
            if items[i] > items[i+1]:   #if this condition is not used, the following values are already swapped.
                # temp = items[i]
                # items[i] = items[i+1]
                # items[i+1] = temp
                items[i], items[i+1] = items[i+1], items[i] # can write in one line

    print(f"steps: {count}")

def bubble_sort_mine2(items: [int]):
    count = 0
    for scan in range(len(items) -1):
        need_swap = False
        for i in range(len(items) -1 - scan):
            count += 1
            if items[i] > items[i+1]:   #if this condition is not used, the following values are already swapped.
                items[i], items[i+1] = items[i+1], items[i] # can write in one line
                need_swap = True
                #print(items)
        if not need_swap:   # no need to check if further elements are already swapped
            break
    print(f"steps: {count}")

def bubble_sort_teacher(items: [int]):
    steps = 0
    for scan in range(len(items) - 1):
        for i in range(len(items) - 1 - scan):
            steps += 1
            if items[i] > items[i+1]:
                # items[i], items[i+1] = items[i+1], items[i]
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp

    print(f"steps: {steps}")

def bubble_sort_teacher_improved(items: [int]):
    steps = 0
    for scan in range(len(items) - 1):
        swapped = False
        for i in range(len(items) - 1 - scan):
            steps += 1
            if items[i] > items[i+1]:
                swapped = True
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp

        if not swapped:
            break
    print(f"steps: {steps}")


a = [5, 1, 3, 2, 4]
#bubble_sort(a)
#print(a)
b = [5, 1, 3, 2, 4]
#bubble_sort_mine(b)
#print(b)

# test
alist = random.sample(range(1, 500), 300)
alist_copy = alist[:]
# alist = [6, 5, 4, 3, 2, 1, 89, 45, 23, 12]
# blist = [6, 5, 4, 3, 2, 1, 89, 45, 23, 12]
b= alist[:]
b2 = alist[:]
bubble_sort_mine(b)
print(b)
bubble_sort_mine2(b2)
print(b2)

bubble_sort_teacher(alist)
bubble_sort_teacher_improved(alist_copy)