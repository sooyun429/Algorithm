import sys
sys.stdin = open('sw5177.txt', 'r')

def minheap(n, cnt):
    if edges[n][1]:
        if edges[edges[n][1]][0] and edges[edges[n][1]][0] < edges[n][0]:
            edges[edges[n][1]][0], edges[n][0] = edges[n][0], edges[edges[n][1]][0]
            cnt += 1
        minheap(edges[n][1], cnt)
    if edges[n][2]:
        if edges[edges[n][2]][0] and edges[edges[n][2]][0] < edges[n][0]:
            edges[edges[n][2]][0], edges[n][0] = edges[n][0], edges[edges[n][2]][0]
            cnt += 1
        minheap(edges[n][2], cnt)
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    edges = [[0, 0, 0] for _ in range(N+1)]
    for i in range(1, len(edges)):
        if i*2 <= N:
            edges[i][1] = i*2
        if i*2+1 <= N:
            edges[i][2] = i*2+1
    for i in range(1, N+1):
        edges[i][0] = numbers[i-1]
        while True:
            check_cnt = minheap(1, 0)
            if check_cnt == 0:
                break
    lastnod = N//2
    result = 0
    while lastnod:
        result += edges[lastnod][0]
        lastnod //=2
    print('#%d %d' % (tc, result))
