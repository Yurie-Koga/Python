from game_data import *
from players import *

# debug mode:
# True = print all notes
is_debug = True


def find_fin(l: []):
    """ find a location that computer can win """
    if is_debug: print(f"l: {l}")
    for i in range(len(l)):
        if is_debug: print(f"l[{i}]: {l[i]}")
        if sum(l[i]) == 2:     # Computer=1, find where Computer has been input to two locations
            for col in range(3):
                if l[i][col] == 0:
                    return i + col
    return -1




def find_block():
    """ find a location that computer can block the player """
    pass

def input_computer(data: [], player: int):
    l = list_horizontal(data)
    fin_ind = find_fin(l)
    if fin_ind >= 0:
        data[fin_ind] = player
        return data

    l = list_vertical(data)
    fin_ind = find_fin(l)
    if fin_ind >= 0:
        data[fin_ind] = player
        return data

    l = list_diagonal_rtl(data)
    fin_ind = find_fin(l)
    if fin_ind >= 0:
        data[fin_ind] = player
        return data

    l = list_diagonal_ltr(data)
    fin_ind = find_fin(l)
    if fin_ind >= 0:
        data[fin_ind] = player
        return data

    for i in range(len(data)):
        if data[i] == 0:
            data[i] = player
            print(f"Computer input @: {i+1}")
            break

    return data


listH = [
        1, 1, 0,
        2, 0, 0,
        2, 1, 1,
    ]
# print(f"{input_computer(listH, 1)}")