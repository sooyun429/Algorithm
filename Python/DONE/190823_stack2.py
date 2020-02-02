## 연습문제 1 후위표기법으로 바꾸는 함수 만들기
def postfix(str):
    operator = {'+': 0, '-': 0, '*': 1, '/': 1}
    stack = []
    for s in str:
        if s not in operator:
            print(s, end='')
        else:
            if stack:
                if operator[stack[-1]] < operator[s]:
                    stack.append(s)
                else:
                    print(stack[-1], end='')
                    stack.pop()
                    stack.append(s)
            else:
                stack.append(s)
    if stack:
        for n in stack:
            print(n, end='')
    else:
        return

## 연습문제 1
def postfix(str):
    operator = {'+': 0, '-': 0, '*': 1, '/': 1}
    stack = []
    for s in str:
        if s not in operator:
            print(s, end='')
        else:
            stack.append(s)
    for n in range(len(stack)):
        print(stack.pop(), end='')
#     return

a = '2+3*4/5'

postfix(a)
