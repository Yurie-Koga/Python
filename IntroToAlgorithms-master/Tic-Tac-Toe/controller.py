from game_data import *
from players import *
from results import *
from computer import *


# debug mode:
# True = print all notes
is_debug = False

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



