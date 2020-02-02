import sys
sys.stdin = open('sw4875.txt', 'r')

def around(i, j):
    global result
    move = [-1, 0, 1, 0, -1]  # 상, 우, 하, 좌 순으로 체크
    for xy in range(4):
        x = i + move[xy]
        y = j + move[xy+1]
        if maze[x][y] == '3':
            result = 1
        elif maze[x][y] == '0':
            maze[x][y] = '1'  # 방문처리
            around(x, y)  # 들어간 위치에서 함수실행해서 주변 체크

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [['1']*(N+2)] + [['1'] + list(input()) + ['1'] for _ in range(N)] + [['1']*(N+2)]
    flag = result = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if maze[i][j] == '2':
                maze[i][j] = '1'
                around(i, j)
                flag = 1
                break
        if flag:
            break
    print('#%d %d' % (tc, result))

