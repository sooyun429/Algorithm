import sys
sys.stdin = open('sw1865.txt', 'r')

## 지희언니 코드 참고
def perm(k, temp=100):
    global maxval
    if k == n:
        if temp > maxval:
            maxval = temp
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            if temp * P[k][arr[k]]/100 > maxval:
                perm(k + 1, temp * P[k][arr[k]]/100)
            arr[k], arr[i] = arr[i], arr[k]


T = int(input())
for tc in range(T):
    n = int(input())
    arr = [i for i in range(n)]
    P = [list(map(int, input().split())) for _ in range(n)]
    maxval = 0
    perm(0)
    print("#%d %f" % (tc + 1, round(maxval, 6)))


## 민기오빠 코드 참고
def makemake(z, summ):
    global max_value
    if z == n:
        if max_value < summ:
            max_value = summ

    else:
        for i in range(n):
            if not visited[i]:
                if max_value < summ * ls[z][i] * 0.01:
                    visited[i] = True
                    makemake(z + 1, summ * ls[z][i] * 0.01)
                    visited[i] = False


for tc in range(1, int(input()) + 1):
    n = int(input())
    max_value = 0
    ls = [list(map(int, input().split())) for _ in range(n)]

    visited = [False] * (n + 1)
    makemake(0, 1)
    round(max_value, 6)
    print('#%d %f' % (tc, max_value * 100))


## itertools, yield 사용하는 방법도 실패(메모리 효율성 떨어짐)
## 참고 링크(https://www.youtube.com/watch?v=hqijNdQTBH8)
# def perm(lst):
#     if len(lst) == 0:
#         yield []
#     elif len(lst) == 1:
#         yield lst
#     else:
#         for i in range(len(lst)):
#             x = lst[i]
#             xs = lst[:i] + lst[i+1:]
#             for p in perm(xs):
#                 yield [x]+p
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     P = [list(map(int, input().split())) for _ in range(N)]
#     arr = [i for i in range(N)]
#     result = 0
#     for p in perm(arr):
#         temp = 100
#         for i in range(N):
#             temp *= P[i][p[i]]/100
#             if temp < result:
#                 break
#         if temp > result:
#             result = temp
#     print('#%d %f' % (tc, round(result, 6)))


## itertools 하면 tc1 정도의 데이터 크기만 가능하고 나머진 메모리 초과됨(실패)
# import itertools
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     P = [list(map(int, input().split())) for _ in range(N)]
#     C = list(itertools.permutations([(i+1) for i in range(N)]))
#     result = 0
#     for i in C:
#         temp = 100
#         for j in range(len(i)):
#             temp *= P[j][i[j]-1] / 100
#         if result < temp:
#             result = temp
#     print('#%d %f' % (tc, round(result, 6)))
