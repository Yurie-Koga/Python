
# debug mode:
# True = print all notes
is_debug = False

# Dictionary of Players:
# 0 : default
# Must pass keys to functions, not values
dic_players = {
    1: "O",
    2: "X",
}


def get_player_value(key: int):
    """ Convert key to value of Players """
    if key in dic_players:
        return dic_players[key]
    else:
        return " "

def get_player_key(value: chr):
    """ Convert value to key of Players """
    for (k, v) in dic_players.items():
        if v == value:
            return k
    return 0


def reset_data() -> []:
    """ Default a game data list """
    return [0] * 9

def list_horizontal(data: []):
    """
    Return a list of horizontal lists
    :param data: a list of a game data
    :return : a list of horizontal lists
    """
    l = []
    for row in range(0, 9, 3):
        c = []
        for col in range(3):
            c.append(data[row + col])
        l.append(c)
        # l.append(data[row:row+3])     # used the same way as other list_ func
    return l

def list_vertical(data: []):
    """
    Return a list of vertical lists
    :param data: a list of a game data
    :return : a list of vertical lists
    """
    l = []
    for col in range(3):
        c = []
        for row in range(0, 9, 3):
            c.append(data[row + col])
        l.append(c)
    return l

def list_diagonal_rtl(data: []):
    """
    Return a list of diagonal lists (Right to Left).
    :param data: a list of a game data
    :return : a list of diagonal lists
    """
    l = []
    row, col = 0, 0
    c = []
    while row < 9 and col < 3:
        c.append(data[row + col])
        row += 3
        col += 1
    l.append(c)
    return l

def list_diagonal_ltr(data: []):
    """
    Return a list of diagonal lists (Left to Right).
    :param data: a list of a game data
    :return : a list of diagonal lists
    """
    l = []
    row, col = 0, 3 - 1
    c = []
    while row < 9 and col >= 0:
        c.append(data[row + col])
        row += 3
        col -= 1
    l.append(c)
    return l

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


def get_input(data: [], player: int) -> int:
    """
    Provide input instructions and return the input value.
    :params data: a list of a game data
    :params player: a key of players
    :return: an integer which is decreased one from the input value to used as list 00_index
    """
    # ex_str = "ex"
    # print(f"== Enter '{ex_str}' to stop running. ==")
    while True:
        try:
            print_data(data)
            inp = input(f"[{get_player_value(player)}] Please make your move! [1-9]: ")
            # if inp.lower() == ex_str:
            #     break

            if int(inp) < 1 or 9 < int(inp):
                raise ValueError
            return int(inp) - 1
        except ValueError:
            print("Invalid Input! Please enter a number.")
        except:
            print("Try again!")

def validate_input(data: [], inp: int, player: int) -> str:
    """
    Set player keys to data list if it is valid.
    Otherwise, return error massages.
    """
    if data[inp] == 0:
        data[inp] = player
        return ""
    elif data[inp] == player:
        return "Already you entered here. Try another!"
    else:
        return "The other player entered here. Try another!"


def print_data(data: []):
    """ Print a list of a game data """
    for row in range(0, 9, 3):
        if row > 0:
            print("---|---|---")
        s = []
        for col in range(3):
            ind = row + col
            # s.append(get_player_value(data[ind][1]))
            s.append(get_player_value(data[ind]))
        print(f" {' | '.join(s)}")


def main_two_players():
    data = reset_data()
    print("Tic-Tac-Toe!")
    print(f"Player1 is {get_player_value(1)} and Player2 is {get_player_value(2)}.")

    p = 1   # default player
    while True:
        inp = get_input(data, p)
        error_msg = validate_input(data, inp, p)
        if error_msg != "":
            print(error_msg)
            continue

        winner = check_result(data)
        if winner < 0:
            print_data(data)
            print("It's a draw!")
            break
        elif winner != 0:
            print_data(data)
            print(f"Congratulations! {get_player_value(winner)} You won!")
            break

        # Switch players
        p = 1 if p == 2 else 2


if __name__ == "__main__":
    main_two_players()