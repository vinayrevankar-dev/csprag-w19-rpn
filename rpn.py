#!/usr/bin/env python3

import operator
import math


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

constants = {
    'pi': math.pi,
    'e': math.e,
    'tau': math.tau,
    'infinity': math.inf,
}

unary = {
    'cos': math.cos,
    'sin': math.sin,
    'tan': math.tan,
    'acos': math.acos,
    'asin': math.asin,
    'atan': math.atan,
}



def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            if token in constants.keys():
                value = constants[token]
                stack.append(value)
                continue
            elif token in unary.keys():
                function = unary[token]
                arg1 = stack.pop()
                result = function(arg1)
                stack.append(result)
                break

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
