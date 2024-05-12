from stack import Stack

def parenthesis(ParSeq):
    S = Stack()
    for p in ParSeq:
        if p == '(': S.push(p)
        elif p == ')': 
            if len(S) > 0: S.pop()
            else: return False
        else: return "Not allowed symbol"
    if len(S) > 0: return False
    else: return True

# input = '(())()()'
# input = '(())('
# input = '(()))'
input = '(()())a'
print(parenthesis(input))