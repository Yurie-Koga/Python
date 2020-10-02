""" Recursion """

# Palindrome is a word, phrase, or sequence that reads the same
# backward as forward.

# Examples)
# is_palindrome(madam) -> True
# is_palindrome(racecar) -> True
# is_palindrome(pizza) -> False

def is_palindrome(word: str) -> bool:
    """
    Check if a given string input (word) is a palindrome.
    You must write your solution recursively. (no loops)
    :param word: string input
    :return: True if word is palindrome, otherwise False
    """
    reversed_word = get_reverse_recur(word, len(word)-1)
    return True if word == reversed_word else False

def get_reverse_recur(word: str, index: int):
    if index < 0 or word == "":
        return ""

    return word[index] + get_reverse_recur(word, index-1)

def get_reverse_loop(word: str):
    res = ""
    for i in range(len(word) - 1, -1, -1):
        # print(f"index: {i}")
        res += word[i]
    return res


if __name__ == "__main__":
    print(get_reverse_loop("test"))
    print(get_reverse_recur("pizza", len("pizza")-1))

    cases = [
        "madam",
        "racecar",
        "pizza",
        "test",
        "baan",
        "baab",
        "",
        "banana",
    ]
    for i in range(len(cases)):
        print(f"{cases[i]} : {is_palindrome(cases[i])}")
