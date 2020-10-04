
# debug mode:
# True = print all notes
is_debug = False

# Dictionary of Players:
# -1: used as a draw
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
    list = []
    for i in range(9):
        list.append([i+1, 0])
    return list

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
    if data[inp][1] == 0:
        data[inp][1] = player
        return ""
    elif data[inp][1] == player:
        return "Already you entered here. Try another!"
    else:
        return "The other player entered here. Try another!"


def get_result_horizontal(data: []):
    """
    Check Winners horizontally.
    :param data: a list of a game data
    :return : a key of winners
    """
    p = 0

    for row in range(0, 9, 3):
        p = 0   # default
        for col in range(3):
            ind = row + col
            if is_debug: print(f"data[{ind+1}, {1}]: {data[ind][1]} ")
            if p == 0 and col == 0:
                p = data[ind][1]
                if is_debug: print(f"p: {p}")
            elif p != data[ind][1]:
                # not same player -> exit -> check other rows
                p = 0
                if is_debug: print("go to next row")
                break
        if p != 0:
            if is_debug: print(f"return p: {p}")
            return p
        if is_debug: print()
    return p

def get_result_vertical(data: []):
    """
    Check Winners vertically.
    :param data: a list of a game data
    :return : a key of winners
    """
    p = 0

    for col in range(3):
        p = 0  # default
        for row in range(0, 9, 3):
            ind = row + col
            if is_debug: print(f"data[{ind+1}, {1}]: {data[ind][1]} ")
            if p == 0 and row == 0:
                p = data[ind][1]
                if is_debug: print(f"p: {p}")
            elif p != data[ind][1]:
                if is_debug: print(f"p: {p}")
                # not same player -> exit -> check other rows
                p = 0
                if is_debug: print("go to next row")
                break
        if p != 0:
            if is_debug: print(f"return p: {p}")
            return p
        if is_debug: print()
    return p

def get_result_diagonal_rtl(data: []):
    """
    Check Winners diagonally (Right to Left).
    :param data: a list of a game data
    :return : a key of winners
    """
    p = 0  # default
    row, col = 0, 0
    while row < 9 and col < 3:
        ind = row + col
        if is_debug: print(f"***** row: {row}, col: {col} *****")
        if is_debug: print(f"data[{ind+1}, {1}]: {data[ind][1]} ")
        if p == 0 and row == 0:
            p = data[ind][1]
            if is_debug: print(f"p: {p}")
        elif p != data[ind][1]:
            if is_debug: print(f"p: {p}")
            p = 0   # not same player -> exit -> check other rows
            if is_debug: print("finish cross")
            return p
        row += 3
        col += 1

    return p

def get_result_diagonal_ltr(data: []):
    """
    Check Winners diagonally (Left to Right).
    :param data: a list of a game data
    :return : a key of winners
    """
    p = 0  # default
    row, col = 0, 3 - 1
    while row < 9 and col >= 0:
        ind = row + col
        if is_debug: print(f"***** row: {row}, col: {col} *****")
        if is_debug: print(f"data[{ind+1}, {1}]: {data[ind][1]} ")
        if p == 0 and row == 0:
            p = data[ind][1]
            if is_debug: print(f"p: {p}")
        elif p != data[ind][1]:
            if is_debug: print(f"p: {p}")
            p = 0   # not same player -> exit -> check other rows
            if is_debug: print("finish cross")
            return p
        row += 3
        col -= 1

    return p

def is_draw(data: []):
    """
    Check if a game is a draw.
    :param data: a list of a game data
    :return : 0 = not a draw, -1 = a draw
    """
    for i in range(len(data)):
        if data[i][1] == 0:
            return 0    # there are still empy items
    return -1   # already full. it's a draw

def check_result(data: []):
    """
    Check results.
    :param data: a list of a game data
    :return : a key of winners or a value of a draw
    """
    p = get_result_horizontal(data)
    if p != 0:
        return p
    p = get_result_vertical(data)
    if p != 0:
        return p
    p = get_result_diagonal_rtl(data)
    if p != 0:
        return p
    p = get_result_diagonal_ltr(data)
    if p != 0:
        return p
    p = is_draw(data)
    if p != 0:
        return p
    return 0



def print_data(data: []):
    """ Print a list of a game data """
    for row in range(0, 9, 3):
        if row > 0:
            print("---|---|---")
        s = []
        for col in range(3):
            ind = row + col
            s.append(get_player_value(data[ind][1]))
        print(f" {' | '.join(s)}")


def run_with_two_players():
    """ Main """
    game_data = reset_data()
    print("Tic-Tac-Toe!")
    print(f"Player1 is {get_player_value(1)} and Player2 is {get_player_value(2)}.")

    p = 1   # default player
    while True:
        inp = get_input(game_data, p)
        error_msg = validate_input(game_data, inp, p)
        if error_msg != "":
            print(error_msg)
            continue

        winner = check_result(game_data)
        if winner < 0:
            print_data(game_data)
            print("It's a draw!")
            break
        elif winner != 0:
            print_data(game_data)
            print(f"Congratulations! {get_player_value(winner)} You won!")
            break

        # Switch players
        p = 1 if p == 2 else 2
    pass


if __name__ == "__main__":
    run_with_two_players()


    # listH= [
    #     [1, 0], [2, 1], [3, 1],
    #     [4, 2], [5, 0], [6, 2],
    #     [7, 1], [8, 1], [9, 1]
    # ]
    # print_data(listH)

    # listH= [
    #     [1, 0], [2, 1], [3, 1],
    #     [4, 2], [5, 0], [6, 2],
    #     [7, 1], [8, 1], [9, 1]
    # ]
    # print(f"list: {listH}")
    # res = get_result_horizontal(listH)
    #
    # listV = [
    #     [1, 1], [2, 2], [3, 1],
    #     [4, 0], [5, 1], [6, 1],
    #     [7, 1], [8, 2], [9, 1],
    # ]
    # print(f"list: {listV}")
    # res = get_result_vertical(listV)
    #
    # listCR = [
    #     [1, 0], [2, 0], [3, 0],
    #     [4, 0], [5, 0], [6, 0],
    #     [7, 0], [8, 0], [9, 0],
    # ]
    # print(f"list: {listCR}")
    # res = get_result_cross_rtl(listCR)
    #
    # listCL = [
    #     [1, 0], [2, 0], [3, 2],
    #     [4, 0], [5, 2], [6, 0],
    #     [7, 1], [8, 0], [9, 0],
    # ]
    # print(f"list: {listCL}")
    # res = get_result_cross_ltr(listCL)
    #
    # print(f"res: {res}")
    # if res == 0:
    #     print("none")
    # elif res == 1:
    #     print("winner: X")
    # elif res == 2:
    #     print("winner: O")

