import sys
sys.stdin = open('sw5105.txt', 'r')


def around(r, c):
    global cnt
    maze[r][c] = '1'
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    for i in range(4):
        if maze[r+dr[i]][c+dc[i]] == '3':
            return 1
        elif maze[r+dr[i]][c+dc[i]] == '0':
            cnt += 1
            if around(r+dr[i], c+dc[i]):
                return 1
            cnt -= 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [[] for _ in range(N)]  # maze 만들기
    start = []
    for n in range(N):
        temp = list(input())
        if start == []:
            for i in range(len(temp)):
                if temp[i] == '2':  # 시작위치 좌표
                    start = [n+1, i+1]
                    break
        maze[n] = ['1'] + temp + ['1']
    maze = [['1']*(N+2)] + maze + [['1']*(N+2)]

    cnt = 0
    around(start[0], start[1])
    print('#%d %d' % (tc, cnt))
