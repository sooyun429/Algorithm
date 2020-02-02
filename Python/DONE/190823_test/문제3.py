import sys
sys.stdin = open('input3.txt', 'r')

def around(a, b, n):
    if land[a][b + 1] in range(1, 51):
        land[a][b + 1] = n
    if land[a + 1][b - 1] in range(1, 51):
        land[a + 1][b - 1] = n
    if land[a + 1][b] in range(1, 51):
        land[a + 1][b] = n
    if land[a + 1][b + 1] in range(1, 51):
        land[a + 1][b + 1] = n

def around2(a, b, n):
    if land[a][b-1]:
        if land[a][b-1] < n:
            land[a][b - 1] = n
        else:
            land[a][b] = land[a][b - 1]
            n = land[a][b]
    if land[a-1][b-1]:
        if land[a-1][b-1] < n:
            land[a - 1][b - 1] = n
        else:
            land[a][b] = land[a - 1][b - 1]
            n = land[a][b]
    if land[a-1][b]:
        if land[a-1][b] < n:
            land[a - 1][b] = n
        else:
            land[a][b] = land[a - 1][b]
            n = land[a][b]
    if land[a-1][b+1]:
        if land[a-1][b+1] < n:
            land[a - 1][b + 1] = n
        else:
            land[a][b] = land[a - 1][b + 1]
            n = land[a][b]

T = int(input())
for tc in range(T):
    N = int(input())
    land = [[0] * (N + 2)] + [([0] + list(map(int, input().split())) + [0]) for _ in range(N)] + [[0] * (N + 2)]
    mark = 100

    for i in range(1, N+1):
        for j in range(1, N+1):
            if land[i][j] in range(1, 51):
                land[i][j] = mark
                around(i, j, mark)
                mark += 100
            elif land[i][j]:
                around(i, j, land[i][j])

    for i in range(N, 0, -1):
        for j in range(N, 0, -1):
            if land[i][j]:
                around2(i, j, land[i][j])

    cnt = {}
    for i in land:
        for j in i:
            if j:
                if j not in cnt:
                    cnt[j] = 1
                else:
                    cnt[j] += 1

    print('#%d %d' % (tc+1, len(cnt)))


