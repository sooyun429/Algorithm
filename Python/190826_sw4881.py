import sys, itertools
sys.stdin = open('sw4881.txt', 'r')


def combination(a):
    global minsum, N, NN
    if len(a) == 2:
        return [a, [a[1], a[0]]]
    else:
        for i in range(len(a)):
            result = a[i] + combination(a[0:i]+a[i+1:])
            cal = 0
            for j in range(len(result)):
                cal += NN[j][result[j]]
            if cal < minsum:
                minsum = cal
        return minsum

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    NN = [list(map(int, input().split())) for _ in range(N)]
    minsum = 10*N
    for i in NN:

    print('#%d %d' % (tc, combination([i for i in range(N)])))


## 런타임에러
# def combination(a):
#     global minsum, N, NN
#     length = len(a)
#     if length == 2:
#         return [a, [a[1], a[0]]]
#     elif length >= 3:
#         temp = combination(a[1:])
#         result = [0]*length*len(temp)
#         idx = 0
#         for i in range(length):
#             for j in range(len(temp)):
#                 result[idx] = temp[j][:i] + [a[0]] + temp[j][i:]  ## 조합 저장
#                 idx += 1
#         if len(result[0]) < N:
#             return result
#         else:
#             for i in result:
#                 cal = 0
#                 for j in range(N):
#                     cal += NN[j][i[j]]
#                 if cal < minsum:
#                     minsum = cal
#             return minsum
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     NN = [list(map(int, input().split())) for _ in range(N)]
#     minsum = 10*N
#     print('#%d %d' % (tc, combination([i for i in range(N)])))



## itertools 사용하면 제한시간 초과
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     NN = [list(map(int, input().split())) for _ in range(N)]
#     comb = itertools.permutations([i for i in range(N)])
#     result = 10*N
#     for i in comb:
#         temp = 0
#         for j in range(len(i)):
#             temp += NN[j][i[j]]
#         if temp < result:
#             result = temp
#     print('#%d %d' % (tc, result))
