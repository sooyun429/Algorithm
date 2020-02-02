import sys
sys.stdin = open('sw1861_test.txt', 'r')


## RecursionError: maximum recursion depth exceeded in comparison
## PyPy로 작동하는 swea 사이트에서는 문제 없음 (interpreter에 따라 오류가 날 때도 있고 없을 때도 있고)
## 풀이 논리성은 맞음

## 세 번째 방법(visited 그냥 1로만 체크)
def around(i, j):
    global NN, cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for k in range(4):
        if NN[i+dx[k]][j+dy[k]] and NN[i][j] + 1 == NN[i+dx[k]][j+dy[k]]:
            cnt += 1
            visited[i+dx[k]][j+dy[k]] = 1
            around(i+dx[k], j+dy[k])
            break


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    NN = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
    minnum = N*N
    result = 0
    visited = [[0]*(N+2) for _ in range(N+2)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            if visited[i][j] != 1:
                cnt = 1
                visited[i][j] = 1
                around(i, j)
                if cnt > result:
                    result = cnt
                    minnum = NN[i][j]
                elif cnt == result:
                    if minnum > NN[i][j]:
                        minnum = NN[i][j]
    print('#%d %d %d' % (tc, minnum, result))



# ## 두 번째 방법(visited check)
# def around(i, j):
#     global NN, cnt
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     nn = NN[i][j]
#     for k in range(4):
#         nnn = NN[i+dx[k]][j+dy[k]]
#         if nnn and nn + 1 == nnn:
#             nnv = visited[i+dx[k]][j+dy[k]]
#             if nnv == 0:
#                 cnt += 1
#                 around(i+dx[k], j+dy[k])
#             else:
#                 cnt += nnv
#             break
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     NN = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
#     minnum = N*N
#     result = 0
#     visited = [[0]*(N+2) for _ in range(N+2)]
#
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if visited[i][j] != 1:
#                 cnt = 1
#                 around(i, j)
#                 visited[i][j] = cnt
#                 if cnt > result:
#                     result = cnt
#                     minnum = NN[i][j]
#                 elif cnt == result:
#                     if minnum > NN[i][j]:
#                         minnum = NN[i][j]
#     print('#%d %d %d' % (tc, minnum, result))



## 첫 번째 방법
# def around(i, j):
#     global NN, cnt
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     flag = 1
#     for k in range(4):
#         if NN[i+dx[k]][j+dy[k]] and NN[i][j] + 1 == NN[i+dx[k]][j+dy[k]]:
#             cnt += 1
#             around(i+dx[k], j+dy[k])
#             flag = 0
#             break
#     if flag:
#         return
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     NN = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
#     minnum = N*N
#     result = 0
#
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             cnt = 1
#             around(i, j)
#             if cnt > result:
#                 result = cnt
#                 minnum = NN[i][j]
#             elif cnt == result:
#                 if minnum > NN[i][j]:
#                     minnum = NN[i][j]
#     print('#%d %d %d' % (tc, minnum, result))
