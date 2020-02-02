import sys
sys.stdin = open('sw4874.txt', 'r')

# 첫 번째 풀이에서 반복구간 줄이기

T = int(input())

for tc in range(1, T+1):
    input_formula = input().split()
    operator = ['+', '-', '*', '/']
    stack = []
    for i in input_formula:
        if i in operator:
            if len(stack) < 2:
                stack[-1] = 'error'
                break
            if i == '+':
                temp = stack[-2] + stack[-1]
                stack.pop()
                stack[-1] = temp
            elif i == '*':
                temp = stack[-2] * stack[-1]
                stack.pop()
                stack[-1] = temp
            elif i == '-':
                temp = stack[-2] - stack[-1]
                stack.pop()
                stack[-1] = temp
            elif i == '/':
                if stack[-1] != 0:
                    temp = stack[-2] // stack[-1]
                    stack.pop()
                    stack[-1] = temp
                else:
                    stack[-1] = 'error'
                    break
        elif i == '.':
            break
        else:
            stack.append(int(i))
    if len(stack) > 1:
        stack[-1] = 'error'
    print('#{} {}'.format(tc, stack[-1]))


# ## 첫 번째 풀이
#
# T = int(input())
#
# for tc in range(1, T+1):
#     input_formula = input().split()
#     stack = []
#     for i in input_formula:
#         if i == '+':
#             if len(stack) >= 2:
#                 temp = stack[-2] + stack[-1]
#                 stack.pop()
#                 stack[-1] = temp
#             else:
#                 stack[-1] = 'error'
#                 break
#         elif i == '*':
#             if len(stack) >= 2:
#                 temp = stack[-2] * stack[-1]
#                 stack.pop()
#                 stack[-1] = temp
#             else:
#                 stack[-1] = 'error'
#                 break
#         elif i == '-':
#             if len(stack) >= 2:
#                 temp = stack[-2] - stack[-1]
#                 stack.pop()
#                 stack[-1] = temp
#             else:
#                 stack[-1] = 'error'
#                 break
#         elif i == '/':
#             if len(stack) >= 2:
#                 if stack[-1] != 0:
#                     temp = stack[-2] // stack[-1]
#                     stack.pop()
#                     stack[-1] = temp
#                 else:
#                     stack[-1] = 'error'
#                     break
#             else:
#                 stack[-1] = 'error'
#                 break
#         elif i == '.':
#             break
#         else:
#             stack.append(int(i))
#     if len(stack) > 1:
#         stack[-1] = 'error'
#     print('#{} {}'.format(tc, stack[-1]))
