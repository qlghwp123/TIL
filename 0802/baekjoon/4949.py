# 192ms
import sys

input = sys.stdin.readline

braket = ['(', ')', '[', ']']
line = input().rstrip()

while line != '.':
    for i in line:
        if i not in braket:
            line = line.replace(i, "")
        line = line.replace("()", "")
        line = line.replace("[]", "")
    
    print("yes" if not line else "no")
    
    line = input().rstrip()

# 112ms 
# https://www.acmicpc.net/source/47065511
# import sys
# lines = sys.stdin.readlines()
# for line in lines[:-1]:
#     stack = []
#     for t in line:
#         if t in '([':
#             stack.append(t)
#         elif t == "]":
#             if not stack or stack.pop() != '[':
#                 print('no')
#                 break
#         elif t == ')':
#             if not stack or stack.pop() != '(':
#                 print('no')
#                 break
#         elif t == '.':
#             if stack:
#                 print('no')
#             else:
#                 print("yes")

# 92ms
# https://www.acmicpc.net/source/47060563
# import sys

# def check_brackets(s):
#     brakets = []
#     for c in s:
#         if c in '([':
#             brakets.append(c)
#         elif c in ')]':
#             if brakets:
#                 left = brakets.pop()
#                 if left == '(' and c == ')':
#                     pass
#                 elif left == '[' and c == ']':
#                     pass
#                 else:
#                     return 'no'
#             else:
#                 return 'no'
#     else:
#         if brakets:
#             return 'no'
#         else:
#             return 'yes'

# while 1:
#     s = sys.stdin.readline().rstrip()
#     if s == '.':    
#         break
#     print(check_brackets(s))