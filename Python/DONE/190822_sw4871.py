import sys
sys.stdin = open('sw4871.txt', 'r')

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())  # 노드 수, 간선 수
    path = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):  # 간선 정보 입력
        a, b = map(int, input().split())
        path[a][b] = b
    for i in range(len(path)):
        path[i] = list(set(path[i]))
        path[i].remove(0)
    # path [[], [3, 4], [3, 5], [], [6], [], []]

    S, G = map(int, input().split())  # Start, Goal

    visited = [0] * (V + 1)  # 노드 방문정보 체크
    visited[S] = 1  # 시작점 방문 체크

    stack = [S]
    while stack:
        if stack[-1] == G:
            break
        if path[stack[-1]]:  # 마지막 위치에서 더 나아갈 수 있는지 체크
            check = 1
            for i in path[stack[-1]]:
                if visited[i] == 0:  # 갈 수 있는 경로 중에 방문한 적 없는 곳으로 간다
                    stack.append(i)  # 들어가는 번호는 스택에 추가해주고
                    visited[i] = 1  # 방문정보에 체크
                    check = 0
                    break  # 그리고 for문은 멈춘다
            if check:
                stack.pop()  # for 문 돌면서 이웃집 방문할 수 있는 곳이 없으면 stack pop
        else:
            if stack:
                stack.pop()
            else:
                break
    if len(stack) == 0:
        result = 0
    elif stack[-1] == G:
        result = 1
    else:
        result = 0
    print('#%d %d' % (tc+1, result))
