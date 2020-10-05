from game_data import *

# debug mode:
# True = print all notes
is_debug = False


def get_result(l: []):
    if is_debug: print(f"l: {l}")
    for i in range(len(l)):
        if is_debug: print(f"l[{i}]: {l[i]}")
        if l[i][0] != 0 and l[i][0] == l[i][1] == l[i][2]:
            return l[i][0]
    return 0

def is_draw(data: []):
    """
    Check if a game is a draw.
    :param data: a list of a game data
    :return : 0 = not a draw, -1 = a draw
    """
    # if 0 is in the data, there are still empty items
    return 0 if 0 in data else -1

def check_result(data: []):
    l = list_horizontal(data)
    p = get_result(l)
    if p != 0:
        return p

    l = list_vertical(data)
    p = get_result(l)
    if p != 0:
        return p

    l = list_diagonal_rtl(data)
    p = get_result(l)
    if p != 0:
        return p

    l = list_diagonal_ltr(data)
    p = get_result(l)
    if p != 0:
        return p

    p = is_draw(data)
    if p != 0:
        return p
    return 0

# l = [
#     1, 0, 0,
#     2, 2, 2,
#     0, 0, 1,
# ]
#
#
# print(check_result(l))

