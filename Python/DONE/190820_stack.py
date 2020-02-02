A = [[0]*10 for _ in range(3)]
print(A)

## stack push pop 만들기 연습문제 1
stack = []

def stack_func(n):
    stack.append(n)
    return print(stack)


def stack_pop():
    if len(stack) == 0:
        return print('nothing')
    return print(stack.pop())

stack_func(1)
stack_func(3)
stack_pop()
print(stack)


## stack 괄호 짝 검사하기 연습문제 2
def check_pairs(p):
    pair_dict = {']': '[', ')': '(', '}': '{'}
    save = []
    for i in p:
        if i in pair_dict.values():
            save.append(i)
        elif i in pair_dict:
            if len(save) == 0:
                return print(False)
            elif save[-1] == pair_dict[i]:
                save.pop()
            else:
                return print(False)
        else:
            continue
    if len(save) == 0:
        return print(True)
    else:
        return print(False)

check_pairs('()()((()))')
check_pairs('((()((((()()((()())((())))))')


## DFS 알고리즘 연습문제 3
ns = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
n = len(set(ns))

## 첫 번째 방법 edge 간선 정보 입력 [[1, 2], [1, 3], [2, 4], [2, 5], [4, 6], [5, 6], [6, 7], [3, 7]]
e = [0] * (len(ns)//2)
for i in range(0, len(ns), 2):
    e[i//2] = [ns[i], ns[i+1]]

## 두 번째 방법 [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
v = [[]] + [[] for _ in range(n)]
for i in range(0, len(ns), 2):
    v[ns[i]].append(ns[i+1])
    v[ns[i+1]].append(ns[i])

## 두 번째 방법을 기본 설정으로 두고 탐색 실행
stack = [1]
visit = [0, 1] + [0] * (n-1)  # [0, 1, 0, 0, 0, 0, 0, 0]
result = [1]
while sum(visit) != n:
    for k in v[stack[-1]]:
        if visit[k] == 0:
            stack.append(k)
            result.append(k)
            visit[k] = 1
            break
        if k == v[stack[-1]][-1]:
            stack.pop()
            break
print(result)
