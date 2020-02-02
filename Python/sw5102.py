import sys
sys.stdin = open('sw5102.txt', 'r')

def path(present, pathMark, level):
    global shortcut
    print(present, pathMark, level)
    pathMark[level] = present
    next = 0
    if edges[present]:
        for i in edges[present]:
            if i == G:
                if 1 < len(pathMark) < len(shortcut):
                    shortcut = pathMark
                    return 1
            elif (i not in pathMark) and edges[i]:
                for j in edges[i]:
                    if j not in pathMark:
                        next = i
                        if path(next, pathMark, level+1):
                if next == 0:
                    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    for i in range(len(edges)):
        if edges[i] == []:
            edges[i] = 0
    S, G = map(int, input().split())
    edges[G] = 0
    print(G, 'edges', edges)
    pathMark = [0] * V
    level = 0
    shortcut = []
    path(S, pathMark, level)
    print('#%d %d' % (tc, len(shortcut)))