
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
