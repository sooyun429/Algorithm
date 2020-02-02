import sys
sys.stdin = open('sw1267.txt', 'r')

for tc in range(1, 11):
    V, E = map(int, input().split())
    N = list(map(int, input().split()))
    edges_out = [[0]*(V+1) for _ in range(V+1)]
    edges_in = [[0]*(V+1) for _ in range(V+1)]
    not_visited = [i for i in range(V+1)]

    for i in range(0, len(N), 2):
        a, b = N[i], N[i+1]
        edges_out[a][b] = 1  # a -> b 방향 선 체크
        edges_in[b][a] = 1  # b로 들어오는 vortex 체크

    stack = []
    while sum(not_visited) > 0:
        for i in not_visited:
            if i:
                if sum(edges_in[i]) == 0: # 들어오는 선이 없는 vortex이면
                    stack.append(str(i))
                    not_visited[i] = 0
                    for j in range(1, V+1):
                        edges_in[j][i] = 0 # 방문한 vortex in표시된 것 제거
    print('#%d %s' % (tc, ' '.join(stack)))
