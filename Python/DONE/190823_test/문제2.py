import sys
sys.stdin = open('test2.txt', 'r')

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    s_max = 0
    for i in range(N-K+1):
        for j in range(M-K+1):
            s_sum = 0
            for n in range(K):
                s_sum += board[i][j+n] + board[i+K-1][j+n] + board[i+n][j] + board[i+n][j+K-1]
            s_sum -= board[i][j] + board[i+K-1][j] + board[i][j+K-1] + board[i+K-1][j+K-1]
            if s_max < s_sum:
                s_max = s_sum
    print('#%d %d' % (tc+1, s_max))
