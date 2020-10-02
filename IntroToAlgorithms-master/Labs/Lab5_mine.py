""" Sorting Practice Problems """

import random

# Write a program that sorts the first half of a list in ascending order
# and the second half in descending order.

# e.g. alist = [8, 1, 7, 5, 2, 4, 2, 9, 3, 6] the alist should be
# changed to   [1, 2, 5, 7, 8, 9, 6, 4, 3, 2]. This should work for other lists of course.

# use bubble or selection sort
def sort_half_bubble_left_to_right(items: [int]):
    step = 0
    for scan in range(len(items) // 2 - 1):
        #print(f"scan ({scan})a: ", end ="")
        step += 1
        for i in range(len(items) // 2 - 1 - scan):
            #print(f"{i} ", end="")
            if items[i] > items[i + 1]:
                items[i], items[i+1] = items[i+1], items[i]
        #print()
    for scan in range(len(items) // 2, len(items) - 1):
        #print(f"scan ({scan}): ", end="")
        step += 1
        for i in range(len(items) // 2, len(items) - 1 - (scan - len(items) // 2)):
            #print(f"{i} ", end="")
            if items[i] < items[i + 1]:
                items[i], items[i+1] = items[i+1], items[i]
        #print()
    #print(f"steps: {step}")
    print(items)
    pass

def sort_half_bubble_out_to_in(items: [int]):
    step = 0
    mid_ind = len(items) // 2
    for scan in range(0, mid_ind):
        #print(f"scan ({scan}): ", end ="")
        step += 1
        for i in range(0, mid_ind - scan - 1):
            #print(f"{i} ", end="")
            if items[i] > items[i + 1]:
                items[i], items[i+1] = items[i+1], items[i]
        #print()
    for scan in range(mid_ind, len(items) - 1):
        #print(f"scan ({scan}): ", end="")
        step += 1
        for i in range(len(items) -1, scan, -1):   # reverse
            #print(f"{i} ", end="")
            if items[i] > items[i - 1]:

                items[i], items[i-1] = items[i-1], items[i]
        #print()
    #print(f"steps: {step}")
    print(items)
    pass

print("--------- sort half ---------")
alist = random.sample(range(1, 500), 20)
#alist = [8, 1, 7, 5, 2, 4, 2, 9, 3, 6]
alist_copy = alist[:]
print("default:")
print(alist)
print("sorted:")
sort_half_bubble_left_to_right(alist)
#print("--------- out to in ---------")
#sort_half_bubble_out_to_in(alist_copy)

# Suppose two lists A and B have already been sorted.
# Elements of A have been sorted into ascending order and
# B has also been sorted in ascending order. Write a Python
# program to merge the elements of A and B into a list.
# At the end of the program the result list will contain
# all the elements of A and B in ascending order.

# read both lists one time
#compare which is smaller -> put smaller one to new list, add ind+1 to smaller one's list
# then compare next elements
def merge_two(A: [int], B: [int]):
    mlist = []
    a = 0
    b = 0
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            mlist.append(A[a])
            a += 1
        elif A[a] == B[b]:
            mlist.append(A[a])
            mlist.append(B[b])
            a += 1
            b += 1
        else:
            mlist.append(B[b])
            b += 1
    for i in range(a - 1, len(A) - 1):
        mlist.append(A[a])
    for i in range(b - 1, len(B) - 1):
        mlist.append(B[b])
    return mlist

print()
print("--------- merge two ---------")
# blist1 = [1, 2, 4, 4]
# blist2 = [5, 5, 6, 7]
blist1 = random.sample(range(1, 20), 10)
blist2 = random.sample(range(1, 20), 10)
blist1.sort()
blist2.sort()
print("default:")
print(blist1, blist2)
print("merged:")
print(merge_two(blist1, blist2))


# Write a program to replace all negative values in a list
# called mylist with zeros. So, if mylist = [2, 5, -1, 3, 7, -2, 8],
# then mylist should be changed to [2, 5, 0, 3, 7, 0, 8]. This
# should of course work for other lists.


def replace_negative_loop(mylist: [int]):
    plist = []
    for i in range(len(mylist)):
        plist.append(get_zero(mylist[i]))
    return plist

def replace_negative_map(mylist: [int]):
    return list(map(get_zero, mylist))

def replace_negative_lambda(mylist: [int]):
    return list(map(lambda x: get_zero(x), mylist))

def get_zero(num: int):
    return 0 if num < 0 else num

print()
print("--------- replace negative ---------")
# clist = [2, 5, -1, 3, 7, -2, 8]
clist = random.sample(range(-10, 20), 10)
print("default:")
print(clist)
print("loop:")
print(replace_negative_loop(clist))
print("map:")
print(replace_negative_map(clist))
print("lambda:")
print(replace_negative_lambda(clist))