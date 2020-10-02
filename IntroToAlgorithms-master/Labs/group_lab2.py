""" Group Lab 2 (in-class) Exhaustive Search, Backtracking """


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


def sum_of_dice(dice: int, desired_sum: int):
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
    # invalid value: seems better to ignore before sum_of_dice_helper
    if dice == 0 or desired_sum <= 0 or desired_sum < dice * 1 or dice * 6 < desired_sum:
        return []

    results = []
    sum_of_dice_helper(dice, desired_sum, [], results)
    # print(results)
    return results

def sum_of_dice_helper(dice: int, desired_sum: int, chosen: [int], results: [int]):
    if dice == 0 and sum(chosen) == desired_sum:
        results.append(chosen.copy())
        return
    elif dice == 0:
        return

    for i in range(1, 7):
        chosen.append(i)
        sum_of_dice_helper(dice - 1, desired_sum, chosen, results)
        chosen.pop()



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

    print("----- sum_of_dice -----")
    cases = [
        (3, 1),
        (3, 30),
        (0, 10),
        (5, 0),
        (1, 3),
        (2, 3),
        (2, 7),
        (3, 5),
    ]
    for i in range(len(cases)):
        print(f"{cases[i]}: {sum_of_dice(cases[i][0], cases[i][1])}")
