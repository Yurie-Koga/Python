""" group exercises 2 """


# Write a recursive function printBinary that accepts integer and
# prints that number's representation in binary (base 2)
#
# Examples:
# print_binary(2)    prints 10
# print_binary(7)    prints 111
# print_binary(12)   prints 1100
# print_binary(42)   prints 101010
# print_binary(-500) prints -111110100
def print_binary_mine(num: int):
    if num == 0:
        print("0", end="")
        return
    elif num < 0:
        print("-", end="")

    numPositive = abs(num)
    if numPositive > 1:
        print_binary_mine(numPositive // 2)
    print(numPositive % 2, end="")

def print_binary(num: int):
    print(print_binary_helper(num))

def print_binary_helper(num: int) -> str:
    if num < 0:
        return "-" + print_binary_helper(num * -1)
    if num == 0:
        return ""
    if num % 2 == 0:
        return print_binary_helper(num // 2) + "0"
    else:
        return print_binary_helper(num // 2) + "1"


# Write a recursive function evaluate that accepts a string
# representing a math expression and computes its value.
# - The expression will be "fully parenthesized" and will
#   consist of + and * on single-digit integers only.
# - You can use a helper function. (Do not change the original function header)
# - Recursion
#
# evaluate("7")                 -> 7
# evaluate("(2+2)"              -> 4
# evaluate("(1+(2*4))"          -> 9
# evaluate("((1+3)+((1+2)*5))") -> 19
# recursively evaluate the same pattern ( left op right )
def eval_helper(expr: str, i: int) -> (int, int):
    if expr[i].isdigit():  # base case
        return int(expr[i]), i
    else:  # recursive case
        i += 1  # skip '('
        left, i = eval_helper(expr, i)
        i += 1  # skip left operand
        op = expr[i]
        i += 1
        right, i = eval_helper(expr, i)
        i += 1  # skip ')'
        if op == '*':
            return left * right, i
        else:
            return left + right, i

def evaluate(expr: str) -> int:
    i = 0
    return eval_helper(expr, i)[0]



# Write a recursive function that accepts an integer number of digits
# and prints all base-10 numbers that have exactly that many digits, in
# ascending order, one per line.
#
# print_decimal(1)  prints from 0 to 9  (single digit)
# print_decimal(2)  prints from 10 to 99 (two digits)
# print_decimal(3)  prints from 100 to 999 (three digits)
def print_decimal_mine(digits: int):
    if digits <= 0:
        return print("0")

    start = get_power_loop(10, digits-1)
    return print(get_decimal(start, digits, []))

def get_power_loop(base: int, exp: int):
    if base <= 0:
        return 0
    res = 1
    for _ in range(exp):
        res *= base
    return res

def get_decimal(start: int, length: int, res: [int]):
    if len(str(start)) > length:
        return res
    res.append(start)
    get_decimal(start+1, length, res)
    return res


def print_decimal(digits: int):
    print_decimal_helper(digits, "", "")

def print_decimal_helper(digits: int, sofar: str, indent: str):
    print(f"{indent}print_decimal_helper({digits}, {sofar})")
    if digits == 0:  # base case, no more digit to print
        print(sofar)
    else:  # recursive
        for i in range(10):
            if sofar != "0":
                print_decimal_helper(digits - 1, sofar + str(i), indent + "    ")


if __name__ == "__main__":
    print("----- binary -----")
    cases = [2, 7, 12, 42, -2, -7, -12, -42, -500, 0]
    for i in range(len(cases)):
        print(f"{cases[i]}: ", end="")
        print_binary_mine(cases[i])
        print()

    print("----- math evalu -----")
    # evaluate("7")                 -> 7
    # evaluate("(2+2)"              -> 4
    # evaluate("(1+(2*4))"          -> 9
    # evaluate("((1+3)+((1+2)*5))") -> 19
    # print(evaluate("((1+3)+((1+2)*5))"))
    cases = [
        "7",
        "(2+2)",
        "(1+(2*4))",
        "((1+3)+((1+2)*5))",
    ]
    for i in range(len(cases)):
        print(f"{cases[i]}: {evaluate(cases[i])}")


    print("----- decimal -----")
    cases = [1, 2, 3]
    for i in range(len(cases)):
        print(f"{cases[i]}:")
        print_decimal_mine(cases[i])