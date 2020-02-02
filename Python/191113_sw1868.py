import sys
sys.stdin = open('sw1868.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    NN = [list(input()) for _ in range(N)]
    for i in NN:
        print(i)
    print('######')
    for i in range(N):
        for j in range(N):
            if NN[i][j]