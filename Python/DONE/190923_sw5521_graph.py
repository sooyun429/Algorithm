## 상원이의 생일파티
import sys
sys.stdin = open('sw5521.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    edges = [[] for _ in range(N+1)]
    lst = []
    for i in range(M):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
        if a == 1: lst.append(b)
        elif b == 1: lst.append(a)

    for i in range(len(lst)):
        for j in edges[lst[i]]:
            if j != 1 and (j not in lst):
                lst.append(j)
    print('#%d %d' % (tc, len(lst)))
