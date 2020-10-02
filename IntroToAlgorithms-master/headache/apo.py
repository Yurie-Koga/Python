import random


def run_one_family() -> (int, int):
    """
    Returns a number of girls and boys in one family by randomly choosing gender
    :return: list of [number of girls, number of boys] in one family
    """
    boys = 0
    girls = 0
    while girls == 0:  # until we have a girl
        # randomly choose between 0:girl and 1:boy
        if random.choice([0, 1]) == 0:
            girls += 1
        else:
            boys += 1

    return girls, boys


def run_n_families(n: int) -> float:
    """
    Returns the gender ratio of the new generation.
    :param n: the number of families
    :return: ratio between girls/boys
    """
    boys = 0
    girls = 0
    for _ in range(n):
        one_family = run_one_family()
        girls += one_family[0]  # num of girls in one fam
        boys += one_family[1]  # num of boys in one fam

    return girls / boys


if __name__ == "__main__":
    for i in range(1000, 2000):  # simulate 1000 to 2000 families
        print(f"ratio(girls/boys) for {i} families: {run_n_families(i)}")