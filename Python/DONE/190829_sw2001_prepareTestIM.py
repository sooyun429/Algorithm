import sys
sys.stdin = open('sw2001.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    NN = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            flies = 0
            if j != 0:
                next = 0
                for k in range(M):
                    next += NN[i+k][j+M-1]
                if prev > next:
                    continue
            prev = 0
            for k in range(M):
                flies += sum(NN[i+k][j:j+M])
                prev += NN[i+k][j]
            if flies > result:
                result = flies

    print('#%d %d' % (tc, result))