

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