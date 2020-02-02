import sys
sys.stdin = open('sw3809.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    D = []
    while True:
        D += input().split()
        if len(D) == N:
            break
    print(D)
    n = 1
    s = 0
    savelist = []
    while n <= N:
        for i in range(N)
        savelist +=

