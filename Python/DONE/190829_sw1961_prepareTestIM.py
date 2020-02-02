import sys
sys.stdin = open('sw1961.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    NN = input().split()
    for _ in range(N-1):
        NN += input().split()
    result90 = [[0] * N for _ in range(N)]
    result180 = [[0] * N for _ in range(N)]
    result270 = [[0] * N for _ in range(N)]
    number = 0
    for i in range(N):
        for j in range(N):
            result90[j][N-1-i] = NN[number]
            result180[N-1-i][N-1-j] = NN[number]
            result270[N-1-j][i] = NN[number]
            number += 1
    result = [0] * N
    print('#%d' % tc)
    for i in range(N):
        print(''.join(result90[i]) + ' ' + ''.join(result180[i]) + ' ' + ''.join(result270[i]))
