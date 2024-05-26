from stack import Stack
# import sys

def calc_elementary(val1, val2, op):
    if op == '+':
        return val2 + val1
    elif op == '-':
        return val2 - val1
    elif op == '*':
        return val2 * val1
    else:
        return val2 / val1


def postfix2val(postfix):
    valstack = Stack()
    for token in postfix:
        try:
            val = float(token)
            valstack.push(val)
        except ValueError:
            if token in '+-*/':
                val1 = valstack.pop()
                val2 = valstack.pop()
                valstack.push(calc_elementary(val1, val2, token))
    return valstack.pop()

# postfix = sys.argv[1]
# val = postfix2val(postfix)
# print(val)
