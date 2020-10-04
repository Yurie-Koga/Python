# Selection Sort
# (pseudo-code)
# for each scan from 0 to len(alist)
#     find the min element (linear search)  : it's unsorted list, unable to use binary search.
#     swap the min element with alist[scan]

# Time Complexity
# O(n^2) algorithm

import random

def selection_sort_original(alist):
    steps = 0
    for scan in range(len(alist) - 1):
        min_index = scan
        for j in range(scan + 1, len(alist)):
            steps += 1
            if alist[min_index] > alist[j]:
                min_index = j

        # swap
        if min_index != scan:
            alist[scan], alist[min_index] = alist[min_index], alist[scan]

    print("steps:", steps)

def selection_sort_(items: [int]):
    count = 0
    swap_step = 0
    for scan in range(len(items) - 1):
        # find min element
        #min_ele = 0 # default value can be items[0]
        #min_ele = items[0]  #then no need to use value. use items[min_ind] instead
        #min_ind = 0
        min_ind = scan # then now scan is the most smallest 00_index in the loop
        # for i in range(len(items) - 1 - scan):    # then now second loop should start from the next 00_index to scan
        for i in range(scan + 1, len(items)):   # NOT "len(items) - 1"
            count += 1
            if items[min_ind] > items[i]:   # leaner search
                min_ind = i

        # swap
        swap_step += 1
        items[scan], items[min_ind] = items[min_ind], items[scan]
    print(f"steps: {count}, swaps: {swap_step}")
    pass

def selection_sort_improved(items: [int]):
    count = 0
    swap_step = 0
    for scan in range(len(items) - 1):
        # find min element
        #min_ele = 0 # default value can be items[0]
        #min_ele = items[0]  #then no need to use value. use items[min_ind] instead
        #min_ind = 0
        min_ind = scan # then now scan is the most smallest 00_index in the loop
        # for i in range(len(items) - 1 - scan):    # then now second loop should start from the next 00_index to scan
        for i in range(scan + 1, len(items)):   # NOT "len(items) - 1"
            count += 1
            if items[min_ind] > items[i]:   # leaner search
                min_ind = i

        # swap
        if min_ind != scan: # no need to swap if the scanning number is the minimum one
            swap_step += 1
            items[scan], items[min_ind] = items[min_ind], items[scan]
    print(f"steps: {count}, swaps: {swap_step}")
    pass



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