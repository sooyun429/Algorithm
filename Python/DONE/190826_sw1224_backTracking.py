import sys
sys.stdin = open('sw1224.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    input_formula = input()
    stack = []
    cal_formula = ''
    for i in input_formula:
        if i == '(':
            stack.append(i)
        elif i == '*':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                cal_formula += stack.pop()
                if len(stack) == 0:
                    break
            stack.pop()  # '(' 괄호 스택에서만 제거
        elif i == '+':
            if len(stack) == 0:
                stack.append(i)
            else:
                while stack[-1] != '(':
                    cal_formula += stack.pop()
                    if len(stack) == 0:
                        break
                stack.append(i)
        else:
            cal_formula += i
    while stack:
        cal_formula += stack.pop()

    for cal in cal_formula:
        if cal == '*':
            temp = stack[-2] * stack[-1]
            stack.pop()
            stack[-1] = temp
        elif cal == '+':
            temp = stack[-2] + stack[-1]
            stack.pop()
            stack[-1] = temp
        else:
            stack.append(int(cal))

    print('#%d %d' % (tc, stack[0]))