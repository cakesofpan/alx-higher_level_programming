#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def op():
    operator = ['+', '-', '*', '/']

    if len(sys.argv) != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator in ['+', '-', '*', '/']:
        if operator == '+':
            res = add(a, b)
        elif operator == '-':
            res = sub(a, b)
        elif operator == '*':
            res = mul(a, b)
        elif operator == '/':
            res = div(a, b)

        print(f"{a} {operator} {b} = {res}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == "__main__":
    op()
