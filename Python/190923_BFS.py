## 연습문제2


def bfs(n):
    global edges, que, result
    visited[n] = 1
    result.append(n)
    que += edges[n]
    while que:
        if visited[que[0]] == 0:
            bfs(que[0])
            que = que[1:]
        else:
            que = que[1:]


N = 7
N = 15
inputdata = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7, 8]
inputdata += [8, 9, 8, 10, 9, 11, 11, 12, 13, 14, 14, 15]
edges = [[] for _ in range(N+1)]
for i in range(0, len(inputdata), 2):
    edges[inputdata[i]].append(inputdata[i+1])
    edges[inputdata[i+1]].append(inputdata[i])
que = []
result = []
visited = [0]*(N+1)
# bfs(1)
# print(result)

for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
print(result)
