"""
 String, List - Level 2.0
"""
import re

def count_hi(string):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.
    """
    return string.count("hi")


def cat_dog(string):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    # return string.count("cat") == string.count("dog")     # This is same as below
    return True if string.count("cat") == string.count("dog") else False


def count_code(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except it'll accept any letter for the 'd', so 'cope' and 'cooe' count.
    """
    return len(re.findall("co.e", string))


def end_other(a, b):
    """
    Given two strings, return True if either of the strings appears at the very end of the other string,
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
    Note: s.lower() returns the lowercase version of a string.
    """
    # match: exactly the same, so should set pattern at the beginning as well
    # both work: ^ and \A, $ and \Z
    patternA = re.compile("^.*" + a + "$", re.IGNORECASE)
    resultA = patternA.match(b)
    patternB = re.compile("^.*" + b + "$", re.IGNORECASE)
    resultB = patternB.match(a)
    return True if resultA is not None or resultB is not None else False


def count_evens(nums):
    """
    Return the number of even ints in the given list.
    Note: the % 'mod' operator computes the remainder, e.g. 5 % 2 is 1.
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            count += 1
    return count
    #return len([num for num in nums if nums % 2 == 0])    # can be written in one line


def big_diff(nums):
    """
    Given a list length 1 or more of ints, return the difference between the largest and smallest values in the array.
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
    """
    return max(nums) - min(nums)


def sum13(nums):
    """
    Return the sum of the numbers in the list, returning 0 for an empty array.
    Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    unlucky = False
    count = 0
    # can be written using while and i += 2 when unlucky
    for i in range(len(nums)):
        if nums[i] == 13:
            unlucky = True
        else:
            if unlucky is True:
                unlucky = False
            else:
                count += nums[i]
    return count


def sum67(nums):
    """
    Return the sum of the numbers in the list, except ignore sections of numbers starting with a 6
    and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
    """
    no_count = False
    count = 0
    for i in range(len(nums)):
        if nums[i] == 6:
            no_count = True
        elif no_count is True:
            no_count = False if nums[i] == 7 else True
        else:
            count += nums[i]
    return count


def has22(nums):
    """
    Given a list of ints, return True if the array contains a 2 next to a 2 somewhere.
    """
    found = False
    for i in range(len(nums)):
        if nums[i] == 2:
            if found is True:
                return True
            else:
                found = True
        else:
            found = False
    return False