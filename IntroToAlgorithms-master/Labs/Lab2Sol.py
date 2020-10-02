"""
Basic python list problems -- no loops.
"""

def first_last6(nums):
    """
    Given a list of ints, return True if 6 appears as either the first or last element in the list.
    The list will be length 1 or more.
    """
    return nums[0] == 6 or nums[-1] == 6


def same_first_last(nums):
    """
    Given a list of ints, return True if the list is length 1 or more, and the first element
    and the last element are equal.
    """
    return True if len(nums) >= 1 and nums[0] == nums[-1] else False


def common_end(a, b):
    """
    Given 2 lists of ints, a and b, return True if they have the same first element or they have the same last element.
    Both lists will be length 1 or more.
    """
    return True if a[0] == b[0] or a[-1] == b[-1] else False


def sum3(nums):
    """
    Given a list of ints length 3, return the sum of all the elements.
    """
    return sum(nums)


def rotate_left3(nums):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
    """
    nums.append(nums.pop(0))
    return nums


def reverse3(nums):
    """
    Given a list of ints length 3, return a new list with the elements in reverse order,
    so {1, 2, 3} becomes {3, 2, 1}.
    """
    nums.reverse()
    return nums


def max_ends3(nums):
    """
    Given a list of ints length 3, figure out which is larger, the first or last element in the list,
    and set all the other elements to be that value. Return the changed list.
    """
    return [nums[0]] * 3 if nums[0] > nums[-1] else [nums[-1]] * 3


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
    return True if nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3 else False