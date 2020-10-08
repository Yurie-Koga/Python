""" Permutation """
def permutation_helper(word: str, sofar: str):
    if len(word) == 0:
        print(sofar)
    else:
        for i in range(len(word)):
            permutation_helper(word[:i] + word[i+1:], sofar + word[i])


def permutation(word: str):
    permutation_helper(word, "")


""" Sum of Dice """
def sum_of_dice_helper(dice: int, desired_sum: int, chosen: [int]):
    if dice == 0:
        if sum(chosen) == desired_sum:
            print(chosen)
    else:
        for i in range(1, 7):
            chosen.append(i)
            sum_of_dice_helper(dice - 1, desired_sum, chosen)
            del chosen[-1]


def sum_of_dice(dice: int, desired_sum: int):
    sum_of_dice_helper(dice, desired_sum, [])


if __name__ == '__main__':
    permutation("park")
    sum_of_dice(2, 7)
