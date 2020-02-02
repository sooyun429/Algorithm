import sys
sys.stdin = open('sw4615.txt', 'r')

def othello(x, y, n):
    global c, d
    i = 1
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, -1, 1, -1, 1]
    while i:  # 오셀로 뒤집기가 가능한지 확인하고 거꾸로 오면서 숫자 바꾸기
        if board[x + dx[n]*i][y + dy[n]*i] == d:
            i += 1
        elif board[x + dx[n]*i][y + dy[n]*i] == c:
            i -= 1
            board[x + dx[n]*i][y + dy[n]*i] = c
        else:
            i = 0

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*(N+2) for _ in range(N+2)]
    board[N//2][N//2] = board[N//2+1][N//2+1] = 2
    board[N//2][N//2+1] = board[N//2+1][N//2] = 1

    for m in range(M):
        a, b, c = map(int, input().split())
        board[b][a] = c
        d = 1 if c == 2 else 2

        for j in range(8):
            # for i in board:
            #     print(i, end='\n')
            # print(j, '###############')
            othello(b, a, j)

    cnt = [0, 0]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 1:
                cnt[0] += 1
            elif board[i][j] == 2:
                cnt[1] += 1
    print('#%d %d %d' % (tc, cnt[0], cnt[1]))
