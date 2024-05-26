from stack import Stack
# import sys

def infix2postfix(expr):
    outstack = []
    opstack = Stack()

    for token in expr:
        try: 
            float(token)
            outstack.append(token)
        except ValueError:
            if token == '(':
                opstack.push(token)
            elif token == ')':
                op = opstack.pop()
                while op != '(':
                    outstack.append(op)
                    op = opstack.pop()
            elif token in '*/':
                opstack.push(token)
            elif token in '+-':
                while len(opstack) != 0:
                    if opstack.top() in '*/':
                        outstack.append(opstack.pop())
                    else:
                        break
                opstack.push(token)

    while len(opstack) != 0:
        outstack.append(opstack.pop())

    return outstack

# infix = sys.argv[1]
# postfix = infix2postfix(infix)
# print(postfix)
