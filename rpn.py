#!/usr/bin/env python3

import operator
import math


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '//': operator.floordiv,
    '&': operator.__and__,
    '|': operator.__or__,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            if token[-1:] == "%":
                percentValue = token[:-1]
                percentValue = stack[0] * (percentValue / 100)
                print(percentValue)
                stack.append(int(percentValue))
                continue
            elif token == '!':
                argument = stack.pop()
                ans = math.factorial(int(argument))
                stack.append(ans)
                continue
            elif token == '~':
                argument = stack.pop()
                ans = ~argument
                stack.append(ans)
                continue

            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
