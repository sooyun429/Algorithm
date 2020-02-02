import sys
sys.stdin = open('sw1486.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    result = 200000
    for i in range(1 << N):
        temp = []
        for j in range(N + 1):
            if i & (1 << j):
                temp.append(H[j])
        if sum(temp) >= B and sum(temp) < result:
            result = sum(temp)
    print('#%d %d' % (tc, result-B))
