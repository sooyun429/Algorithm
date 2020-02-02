import sys
sys.stdin = open('test1.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    board = [[0]*(N+1) for _ in range(N+1)]
    info = [[] for _ in range(M)]
    for n in range(M):  # info = [[2, 3, 4, 6], [4, 2, 7, 4], [7, 4, 8, 7]] 좌표정보
        info[n] = list(map(int, input().split()))
    for n in info:
        for r in range(n[0], n[2]+1):
            for c in range(n[1], n[3]+1):
                board[r][c] = 1
    result = 0
    for i in board:
        result += sum(i)
    print('#%d %d' % (tc+1, result))
