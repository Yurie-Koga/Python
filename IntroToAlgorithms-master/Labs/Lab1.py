"""
Basic python string problems -- no loops.
"""


def hello_name(name):
    """
    Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
    """
    return "Hello " + name + "!"


def make_tags(tag, word):
    """
    The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text.
    In this example, the "i" tag makes <i> and </i> which surround the word "Yay".
    Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
    """
    return "<" + tag + ">" + word + "</" + tag + ">"


def first_two(string):
    """
    Given a string, return the string made of its first two chars, so the String "Hello" yields "He".
    If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string ""
    yields the empty string "".
    """
    return string[:2]


def first_half(string):
    """
    Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
    """
    return string[:(len(string)//2)]


def without_end(string):
    """
    Given a string, return a version without the first and last char, so "Hello" yields "ell".
    The string length will be at least 2.
    """
    return string[1:len(string)-1]


def non_start(a, b):
    """
    Given 2 strings, return their concatenation, except omit the first char of each.
    The strings will be at least length 1.
    """
    return a[1:] + b[1:]


def left2(string):
    """
    Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
    The string length will be at least 2.
    """
    return string[2:] + string[:2]


if __name__ == "__main__":
    print("----- hello_name -----")
    cases = [
        ("Bob", "Hello Bob!"),
        ("X", "Hello X!"),
        ("Derrick", "Hello Derrick!"),
        ("Alpha", "Hello Alpha!"),
        ("Van couver", "Hello Van couver!"),
        ("xyz!", "Hello xyz!!"),
    ]
    for i in range(len(cases)):
        print(f"{cases[i][0]}: {hello_name(cases[i][0])}")

    print("----- make_tags -----")
    cases = [
        ("i", "Yay", "<i>Yay</i>"),
        ("p", "Hello", "<p>Hello</p>"),
        ("img", "here", "<img>here</img>"),
        ("body", "Heart", "<body>Heart</body>"),
        ("h1", "", "<h1></h1>"),
        ("a", "a", "<a>a</a>"),
    ]
    for i in range(len(cases)):
        print(f"{cases[i][0]}, {cases[i][1]}: {make_tags(cases[i][0], cases[i][1])}")

    print("----- first_two -----")
    cases = [
        ("Hello", "He"),
        ("abcdefg", "ab"),
        ("a bcd", "a "),
        ("a", "a"),
        ("", ""),
        ("hi", "hi"),
    ]
    for i in range(len(cases)):
        print(f"{cases[i][0]}: {first_two(cases[i][0])}")

    print("----- first_half -----")
    cases = [
        ("WooHoo", "Woo"),
        ("HelloThere", "Hello"),
        ("ab", "a"),
        ("", ""),
        ("0123456789", "01234"),
        ("abcd", "ab"),
    ]
    for i in range(len(cases)):
        print(f"{cases[i][0]}: {first_half(cases[i][0])}")

    print("----- without_end -----")
    cases = [
        ("Hello", "ell"),
        ("java", "av"),
        ("coding", "odin"),
        ("code", "od"),
        ("ab", ""),
        ("Yeah!", "eah"),
    ]
    for i in range(len(cases)):
        print(f"{cases[i][0]}: {without_end(cases[i][0])}")

    print("----- non_start -----")
    cases = [
        ("Hello", "There", "ellohere"),
        ("Python", "Code", "ythonode"),
        ("ab", "xy", "by"),
        ("ab", "x", "b"),
        ("x", "ac", "c"),
        ("a", "x", ""),
    ]
    for i in range(len(cases)):
        print(f"{cases[i][0]}, {cases[i][1]}: {non_start(cases[i][0], cases[i][1])}")

    print("----- left2 -----")
    cases = [
        ("Hello", "lloHe"),
        ("Hi", "Hi"),
        ("python", "thonpy"),
        ("cat", "tca"),
        ("12345", "34512"),
        ("bricks", "icksbr"),
    ]
    for i in range(len(cases)):
        print(f"{cases[i][0]}: {left2(cases[i][0])}")