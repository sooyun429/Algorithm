import sys
sys.stdin = open('sw5174.txt', 'r')

def child(n):
    global stack
    stack += [n]
    if edges[n][0]:
        child(edges[n][0])
    if edges[n][1]:
        child(edges[n][1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    info = list(map(int, input().split()))
    edges = [[0, 0] for _ in range(E+2)]
    for i in range(0, len(info), 2):
        if edges[info[i]][0]:
            edges[info[i]][1] = info[i+1]
        else:
            edges[info[i]][0] = info[i+1]
    stack = []
    child(N)
    print('#%d %d' % (tc, len(stack)))
