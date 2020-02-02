import sys
sys.stdin = open('sw5178.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    edges = [[0, 0, 0] for _ in range(N+1)]
    for i in range(1, len(edges)):
        if i*2 <= N:
            edges[i][1] = i*2
        if i*2+1 <= N:
            edges[i][2] = i*2+1
    for i in range(M):
        a, b = map(int, input().split())
        edges[a][0] = b
    for i in range(N, 0, -1):
        if edges[i][1] + edges[i][2]:
            if edges[i][2] == 0:
                edges[i][0] = edges[edges[i][1]][0]
            else:
                edges[i][0] = edges[edges[i][1]][0] + edges[edges[i][2]][0]
    print('#%d %d' % (tc, edges[L][0]))
