"""
Basic python list problems -- no loops.
"""


def first_last6(nums):
    """
    Given a list of ints, return True if 6 appears as either the first or last element in the list.
    The list will be length 1 or more.
    """
    return True if nums[0] == 6 or nums[len(nums)-1] == 6 else False

def same_first_last(nums):
    """
    Given a list of ints, return True if the list is length 1 or more, and the first element
    and the last element are equal.
    """
    if len(nums) < 1:
        return False
    return True if nums[0] == nums[len(nums)-1] else False


def common_end(a, b):
    """
    Given 2 lists of ints, a and b, return True if they have the same first element or they have the same last element.
    Both lists will be length 1 or more.
    """
    return True if a[0] == b[0] or a[len(a)-1] == b[len(b)-1] else False


def sum3(nums):
    """
    Given a list of ints length 3, return the sum of all the elements.
    """
    return sum(nums)


def rotate_left3(nums):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
    """
    # res.append(nums[1:])  # this will add a list of list
    res = nums[1:]
    res.append(nums[0])
    return res


def rotate_left3_better_way(nums):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
    """
    # what is happening when append and pop are being used in the same line:
    # res = nums
    # popped = res.pop(0)
    # print(f"res: {res}, popped: {popped}")
    # res.append(popped)

    nums.append(nums.pop(0))
    return nums
    # return nums.append(nums.pop(0))   # does not work. return None.

# print("better way")
# i = [1, 2, 3]
# print(rotate_left3_better_way(i))


def reverse3(nums):
    """
    Given a list of ints length 3, return a new list with the elements in reverse order,
    so {1, 2, 3} becomes {3, 2, 1}.
    """
    # both work.
    # return nums[len(nums)-1::-1]
    # return nums[-1::-1]

    nums.reverse()
    return nums

def max_ends3(nums):
    """
    Given a list of ints length 3, figure out which is larger, the first or last element in the list,
    and set all the other elements to be that value. Return the changed list.
    """
    if nums[0] > nums[len(nums) - 1]:
        return list(map(lambda x: nums[0], nums))
        # return [nums[0] for x in nums]    # both work
    else:
        return list(map(lambda x: nums[-1], nums))
        # return [nums[-1] for x in nums]

# don't know how to write using map
# def max_ends3_map(nums):
#     return list(map(larger(nums[0], nums[-1]), nums))
#
# def larger(a, b):
#     return a if a > b else b

def make_ends(nums):
    """
    Given a list of ints, return a new list length 2 containing the first and last elements from the original list.
    The original list will be length 1 or more.
    """
    return [nums[0], nums[-1]]


def has23(nums):
    """
    Given an int list length 2, return True if it contains a 2 or a 3.
    """
    return True if 2 in nums or 3 in nums else False


if __name__ == "__main__":
    print("----- first_last6 -----")
    cases = [
        ([1, 2, 6], True),
        ([6, 1, 2, 3], True),
        ([13, 6, 1, 2, 3], False),
        ([3, 2, 1], False),
        ([6], True),
        ([3], False),
        ([5, 6], True),
        ([5, 5], False),
    ]
    for i in range(len(cases)):
        print(f"{cases[i][0]}: {first_last6(cases[i][0])}")

    print("----- same_first_last -----")
    cases = [
        ([1, 2, 3], False),
        ([1, 2, 3, 1], True),
        ([7], True),
        ([], False),
        ([7, 7], True),
        ([1, 2, 3, 4, 5, 1], True),
        ([1, 2, 3, 4, 5, 13], False),
    ]
    for i in range(len(cases)):
        print(f"{cases[i][0]}: {same_first_last(cases[i][0])}")

    print("----- common_end -----")
    cases = [
        ([1, 2, 3], [7, 3], True),
        ([1, 2, 3], [7, 3, 2], False),
        ([1, 2, 3], [1, 3], True),
        ([1, 2, 3], [1], True),
        ([1, 2, 3], [2], False),
    ]
    for i in range(len(cases)):
        print(f"{cases[i][0]}, {cases[i][1]}: {common_end(cases[i][0], cases[i][1])}")

    print("----- sum3 -----")
    cases = [
        ([1, 2, 3], 6),
        ([5, 11, 2], 18),
        ([7, 0, 0], 7),
        ([1, 2, 1], 4),
        ([1, 1, 1], 3),
        ([2, 7, 2], 11),
    ]
    for i in range(len(cases)):
        print(f"{cases[i][0]}: {sum3(cases[i][0])}")

    print("----- rotate_left3 -----")
    cases = [
        ([1, 2, 3], [2, 3, 1]),
        ([5, 11, 9], [11, 9, 5]),
        ([7, 0, 0], [0, 0, 7]),
        ([1, 2, 1], [2, 1, 1]),
        ([0, 0, 1], [0, 1, 0]),
    ]
    for i in range(len(cases)):
        print(f"{cases[i][0]}: {rotate_left3(cases[i][0])}")

    print("----- reverse3 -----")
    cases = [
        ([7], [7]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([7, 2, 3], [3, 2, 7]),
        ([1, 2, 3], [3, 2, 1]),
        ([7, 0, 0], [0, 0, 7]),
        ([2, 1, 2], [2, 1, 2]),
        ([2, 11, 3], [3, 11, 2]),
        ([0, 6, 5], [5, 6, 0]),
        ([7, 2, 3], [3, 2, 7]),
    ]
    for i in range(len(cases)):
        print(f"{cases[i][0]}: {reverse3(cases[i][0])}")

    print("----- max_ends3 -----")
    cases = [
        ([1, 2, 3], [3, 3, 3]),
        ([11, 5, 9], [11, 11, 11]),
        ([2, 11, 3], [3, 3, 3]),
        ([3, 11, 11], [11, 11, 11]),
        ([2, 11, 2], [2, 2, 2]),
        ([0, 0, 1], [1, 1, 1]),
    ]
    for i in range(len(cases)):
        print(f"{cases[i][0]}: {max_ends3(cases[i][0])}")
    # print("----- max_ends3 (map) -----")
    # for i in range(len(cases)):
    #     print(f"{cases[i][0]}: {max_ends3_map(cases[i][0])}")

    print("----- make_ends -----")
    cases = [
        ([1, 2, 3], [1, 3]),
        ([1, 2, 3, 4], [1, 4]),
        ([1, 2, 2, 2, 2, 2, 2, 3], [1, 3]),
        ([7, 4], [7, 4]),
        ([7], [7, 7]),
        ([5, 2, 9], [5, 9]),
        ([2, 3, 4, 1], [2, 1]),
    ]
    for i in range(len(cases)):
        print(f"{cases[i][0]}: {make_ends(cases[i][0])}")

    print("----- has23 -----")
    cases = [
        ([2, 5], True),
        ([5, 2], True),
        ([2, 3], True),
        ([4, 3], True),
        ([4, 5], False),
        ([3, 3], True),
        ([7, 7], False),
    ]
    for i in range(len(cases)):
        print(f"{cases[i][0]}: {has23(cases[i][0])}")

