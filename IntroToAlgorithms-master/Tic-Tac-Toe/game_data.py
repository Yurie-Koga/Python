

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