from infix2postfix import infix2postfix
from postfix2val import postfix2val
import sys

infix = sys.argv[1]
# print(infix)
postfix = infix2postfix(infix)
# print(postfix)
val = postfix2val(postfix)
print(val)