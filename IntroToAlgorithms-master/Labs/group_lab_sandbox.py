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
def print_binary(num: int):
    if num == 0:
        print("0", end="")
        return
    elif num < 0:
        print("-", end="")

    numPositive = abs(num)
    if numPositive > 1:
        print_binary(numPositive // 2)
    print(numPositive % 2, end='')



def print_binary_(num: int):
    bin = get_binary(num)
    if num == 0:
        print("0")
    elif num > 0:
        print(bin)
    else:
        print("-" + bin)

def get_binary(num: int) -> str:
    nPositive = abs(num)
    res = ""
    if nPositive > 1:
        res += get_binary(nPositive // 2)
    res += str(nPositive % 2)
    return res

"""
def print_binary_resolt(num):
  if num < 0:
    print('-', end='')
  print_binary(num)
def print_binary(num):
    number = abs(num)
    if number > 1:
        print_binary(number // 2)
    print(number % 2, end='')
"""

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
# operand: number
# operater: +, -
dic={"+": lambda x, y:x+y,
     "-": lambda x, y:x-y,
     "/": lambda x, y:x/y,
     "%": lambda x, y:x%y,
     "*": lambda x, y:x*y}
def evaluate(expr: str, op=None, nums=None):
    if expr != "":
        op = op if op else []
        nums = nums if nums else []
        item = expr[0]
        if item in ("+", "-", "%", "/", "*"):
            op.append(item)
        elif item.isdigit():
            nums.append(item)
        elif item == ")":
            operator = op.pop()
            opd1, opd2 = int(nums.pop()), int(nums.pop())
            ans = dic[operator](opd1, opd2)
            nums.append(ans)
        return evaluate(expr[1:], op, nums)
    else:
        if op and nums:
            operator = op.pop()
            opd1, opd2 = int(nums.pop()), int(nums.pop())
            return dic[operator](opd1, opd2)
        else:
            return nums[-1]


# Write a recursive function that accepts an integer number of digits
# and prints all base-10 numbers that have exactly that many digits, in
# ascending order, one per line.
#
# print_decimal(1)  prints from 0 to 9  (single digit)
# print_decimal(2)  prints from 10 to 99 (two digits)
# print_decimal(3)  prints from 100 to 999 (three digits)
def print_decimal(digits):
    digits_list = []
    if digits == 0:
        return []
    if digits == 1:
        power = 0
    else:
        power = 10 ** (digits - 1)

    start = 10 ** digits
    end = 10 ** (digits - 1)
    print()
    print(f"power: {power}, start: {start}, end: {end}")

    # start = 10 ** (digits - 1)
    # end = 10 ** digits
    # end = 10 ** (digits - 1)
    # print(f"start: {start}, end: {end}")
    for i in range(power, start, end):
    # for i in range(start, end):
        print(f"i: {i}")
        digits_list.append(i)
        print(f"after i: {list(dict.fromkeys(digits_list))}")
        for j in print_decimal(digits - 1):
            print(f"i: {i}, j: {j}, i+j: {i+j}")
            digits_list.append(i + j)
            print(f"after j: {list(dict.fromkeys(digits_list))}")
    return list(dict.fromkeys(digits_list))
print("aaaaaaa")
print(print_decimal(1))
print(print_decimal(2))


def print_decimal_(digits):
    start = power_recur(10, digits - 1)     # start: 10^(n-1)
    end = power_recur(10, digits) - 1       # end: 10^n - 1
    # print(f"start: {start}, end: {end}")
    res = []
    for i in range(start, end + 1):
        res.append(i)
    print(res)

def power_recur(base: int, exp: int):
    if exp <= 0:
        return 1
    return base * power_recur(base, exp-1)

def print_decimal_recur(digits: int):
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
        return
    res.append(start)
    get_decimal(start+1, length, res)
    return res




print("----- decimal -----")
print_decimal_recur(1)
print_decimal_recur(2)

# if __name__ == "__main__":
    # print("----- binary -----")
    # cases = [2, 7, 12, 42, -2, -7, -12, -42, -500, 0]
    # for i in range(len(cases)):
    #     print(f"{cases[i]}: ", end="")
    #     print_binary(cases[i])
    #     print()
    #
    # print("----- math evalu -----")
    # # evaluate("7")                 -> 7
    # # evaluate("(2+2)"              -> 4
    # # evaluate("(1+(2*4))"          -> 9
    # # evaluate("((1+3)+((1+2)*5))") -> 19
    # # print(evaluate("((1+3)+((1+2)*5))"))
    # cases = [
    #     "7",
    #     "(2+2)",
    #     "(1+(2*4))",
    #     "((1+3)+((1+2)*5))",
    # ]
    # for i in range(len(cases)):
    #     print(f"{cases[i]}: {evaluate(cases[i])}")
    #
    #
    # print("----- decimal -----")
    # cases = [1, 2, 3]
    # for i in range(len(cases)):
    #     print(f"{cases[i]}:")
    #     print_decimal(cases[i])