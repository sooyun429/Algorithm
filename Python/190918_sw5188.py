import sys
sys.stdin = open('sw5188.txt', 'r')

def around(i, j, sum):
    global visited, result

    if i == N and j == N:
        if sum + NN[i][j] < result:
            result = sum + NN[i][j]
            return
    else:
        dx = [0, 1]
        dy = [1, 0]
        for n in range(2):
            # if NN[i + dx[n]][j + dy[n]] and (not visited[i + dx[n]][j + dy[n]]):
            if NN[i+dx[n]][j+dy[n]] and sum + NN[i+dx[n]][j+dy[n]] < result:
                sum += NN[i+dx[n]][j+dy[n]]
                # visited[i+dx[n]][j+dy[n]] = 1
                around(i+dx[n], j+dy[n], sum)
                # visited[i+dx[n]][j+dy[n]] = 0
                sum -= NN[i+dx[n]][j+dy[n]]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    NN = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
    print(NN)
    visited = [[0]*(N+2) for _ in range(N+2)]
    visited[1][1] = 1
    result = 20 * N
    around(1, 1, NN[1][1])
    print('#%d %d' % (tc, result))

