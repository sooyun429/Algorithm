import sys
sys.stdin = open('bj1244.txt', 'r')

N = int(input())
switches = list(map(int, input().split()))
s_num = int(input())
for i in range(s_num):
    a, b = map(int, input().split())
    if a == 1:
        for j in range(N):
            if (j+1)%b == 0:
                switches[j] = (switches[j]+1)%2
    else:
        j = 1
        while b - 1 + j < N and b - 1 - j >= 0:
            if switches[b-1+j] == switches[b-1-j]:
                j += 1
            else:
                break
        switches[b-1] = (switches[b-1]+1)%2
        for k in range(1, j):
            switches[b-1-k] = (switches[b-1-k]+1)%2
            switches[b-1 + k] = (switches[b-1 + k] + 1) % 2
idx = 0
while idx < len(switches):
    print(str(switches[idx]), end=' ')
    idx += 1
    if idx%20 == 0:
        print()
