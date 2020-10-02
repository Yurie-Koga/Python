""" Group Lab 2 (in-class) Exhaustive Search, Backtracking """

from typing import List


def permutation(word: str):
    """
    Write a recursive function permutation that accepts a string as a parameter
    and outputs all possible rearrangements of the letters in the string.
    The arrangements may be output in any order.
    example)
    permutation("park")
    output: park, pakr, pkar, prak, arpk, aprk, akrp, ...
    :param word: word to permute
    :return: display permutations of a given word
    """
    if len(word) == 0:
        return ['']
    pre = permutation(word[1:len(word)])
    next = []
    for i in range(0, len(pre)):
        for j in range(0, len(word)):
            nextString = pre[i][0:j] + word[0] + pre[i][j:len(word) - 1]
            if nextString not in next:
                next.append(nextString)
    # print(next)
    return next


# def permutation_loop(word: str):
#     for i in range(len(word)):
#         target_chr = word[i]    # "p" of "park"
#         for j in range(i+1, len(word)): # "ark" of "park"
#
#     pass

def get_permutation_loop(word: str):
    for i in range(len(word)):
        parent = word[i]
        child = word[0:i] + word[i + 1:len(word)]
        print(f"parent: {parent}, chile: {child}")
        for j in range(i + 1, len(word)):
            print(parent + word[i + 1:j] + word[j + 1:len(word)])
    pass


# get_permutation_loop("park")

def sum_of_dice_loop(dice: int, desired_sum: int):
    """
    Prints all possible outcomes of rolling the given number of six-sided dice
    that add up to the given desired sum, in {#, #, #} format.

    :param dice: the number of dice
    :param desired_sum: desired sum
    :return: display all possible ways
    example)
    sum_of_dice(2, 7)
    output: {1, 6}, {2, 5}, {3, 4}, {4, 3}, {5, 2}, {6, 1}

    """

    list = []
    for d in range(dice):
        list.append([1, 2, 3, 4, 5, 6])

    print(list)
    print(len(list), len(list[0]))
    for i in range(len(list)):  # dice=3, then len=3
        for j in range(len(list[i])):  # len of each list=6

    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == desired_sum:
                list.append([i, j])
    print(list)


print("----- dice loop -----")
sum_of_dice_loop(2, 7)


def sum_of_dice_recur(dice: int, desired_sum: int):
    print(sum_of_dice_recur_helper(dice, desired_sum, []))


def sum_of_dice_recur_helper(dice: int, desired_sum: int, current: [int]):
    if dice <= 0 or desired_sum <= 0:
        return
    if dice == 1 and desired_sum > 6:  # invalid desired_sum, impossible
        return
    if dice == 1 and desired_sum <= 6:  # recursion will be end here
        for i in range(len(current)):
            print(f"({current[i]}, {desired_sum})", end="")
        return
        # return desired_sum  # remains are only desired_sum
    else:  # needs to recursion again
        res = []
        for i in range(1, 7):
            if desired_sum - i >= 0:
                current.append(i)
                sum_of_dice_recur_helper(dice - 1, desired_sum - i, current)
                # res.append([i, sum_of_dice_recur_helper(dice - 1, desired_sum - i)])
                # print(f"list: {list}")
                # for j in range(list):
                #     curList = list[j]
                #     for k in range(len(curList)):
                #         res.append([i, curList[k]])
        # return res


# sum_of_dice_recur(2, 3)

DiceResult = List[List[int]]


def dice_sum(num_dice: int, target_sum: int):
    results = []
    dice_sum_helper(num_dice, target_sum, [], results)
    print(results)


def dice_sum_helper(num_dice: int, target_sum: int, chosen: List[int], results: DiceResult):
    if num_dice == 0 and sum(chosen) == target_sum:
        # Store the value that meets the constraints
        results.append(chosen.copy())
    elif num_dice == 0:
        return
    else:
        for i in range(1, 7):
            chosen.append(i)
            dice_sum_helper(num_dice - 1, target_sum, chosen, results)
            chosen.pop()


dice_sum(3, 7)

if __name__ == "__main__":
    print("----- permutation -----")
    cases = [
        "a",
        "ab",
        "one",
        "park",
    ]
    for i in range(len(cases)):
        print(f"{cases[i]}: {permutation(cases[i])}")

    print("----- permutation -----")

