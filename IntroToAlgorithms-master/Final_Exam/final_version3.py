""" Final Exam V3 """


# please submit your python file upon completion.

def is_anagram(s: str, t: str):
    """
    An anagram is a word or phrase formed by rearranging the
    letters of a different word or phrase, typically using all
    the letters exactly once.

    Given two strings s and t, write a program to
    determine if t is an anagram of s.
    You may assume that the string contains only lowercase alphabets.

    e.g.
    is_anagram("anagram", "nagaram") -> True
    is_anagram("rat", "car") -> False
    is_anagram("listen", "silent") -> True
    is_anagram("", "") -> True
    is_anagram("h", "e") -> False

    :param s: string
    :param t: string
    :return: True if s is an anagram of t, otherwise False
    """
    if len(s) != len(t):
        return False
    if s == t:
        return True

    for i in range(len(s)):
        if s.count(s[i]) != t.count(s[i]):
            return False
    return True

def is_anagram_way2(s: str, t: str):
    if len(s) != len(t):
        return False
    if s == t:
        return True

    new_s, new_t = s, t
    for i in range(len(s)):
        new_s = new_s.replace(s[i], "")
        new_t = new_t.replace(s[i], "")
        if len(new_s) != len(new_t):
            # print(f"exit due to the length. s: {s}, t: {t}")
            return False

    return True if new_s == new_t == "" else False

def remove_vowels(s: str):
    """
    Write an algorithm to remove all vowels from a string without replace() built-in method.
    You can write iteratively or recursively.

    e.g.
    remove_vowels("hello") -> "hll"
    remove_vowels("world") -> "wrld"
    remove_vowels("what") -> "wht"
    remove_vowels("") -> ""
    remove_vowels("a") -> ""

    :param s: string
    :return: string removed vowels
    """
    if s == "":
        return s

    l_vowels = ["a", "e", "i", "o", "u"]
    res = ""
    for i in range(len(s)):
        if s[i] not in l_vowels:
            res += s[i]
    return res

def remove_vowels_way2(s: str):
    if s == "":
        return s

    res = s
    l_vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(l_vowels)):
        res = res.replace(l_vowels[i], "")
    return res


if __name__ == "__main__":
    print("----- is anagram -----")
    cases = [
        ["12", "123"],
        ["", ""],
        ["tomato", "tomato"],
        ["tat", "att"],
        ["tamago", "ogamat"],
        ["banana", "banann"],
        ["tow", "two"],
        ["tttti", "ttttti"],
        ["abcde", "abcdf"],
    ]
    print("----- way1 -----")
    for i in range(len(cases)):
        print(f"{cases[i]}: ", is_anagram(cases[i][0], cases[i][1]))

    print("----- way2 -----")
    for i in range(len(cases)):
        print(f"{cases[i]}: ", is_anagram_way2(cases[i][0], cases[i][1]))

    print("----- remove vowels -----")
    cases = [
        "tat",
        "tet",
        "tit",
        "tot",
        "tut",
        "tatutaaa",
        "tsjkhg",
    ]
    print("----- way1 -----")
    for i in range(len(cases)):
        print(f"{cases[i]}: ", remove_vowels(cases[i]))

    print("----- way2 -----")
    for i in range(len(cases)):
        print(f"{cases[i]}: ", remove_vowels_way2(cases[i]))
