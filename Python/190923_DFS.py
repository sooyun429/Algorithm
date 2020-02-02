## 연습문제 1
## 다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열해 놓은 것이다.
## 모든 정점을 깊이 우선 탐색하여 화면에 깊이우선탐색 경로를 출력하시오.
## 시작 정점을 1로 시작하시오.

inputdata = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
## 출력 결과의 예는 다음과 같다.
## 1-2-4-6-5-7-3
## 1-3-7-6-5-2-4

## 재귀문 활용한 DFS
def iterdfs(n, visited, stack):
    global result
    visited[n] = 1
    stack.append(n)
    temp = edges[n]
    if sum(visited) == N and (stack not in result):
        result.append(stack)
    if temp:
        print(edges[n], visited, stack)
        if visited[temp[-1]] == 0:
            iterdfs(temp[-1], visited, stack)
            temp.pop()
        else:
            temp.pop()
            iterdfs(temp[-1], visited, stack)


N = 7
edges = [[] for _ in range(N+1)]
for i in range(0, len(inputdata), 2):
    edges[inputdata[i]].append(inputdata[i+1])
    edges[inputdata[i+1]].append(inputdata[i])
print(edges)
result = []
iterdfs(1, [0]*(N+1), [])
print(result)
