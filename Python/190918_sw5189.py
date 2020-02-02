import sys
sys.stdin = open('sw5189.txt', 'r')

# def perm(k, sum = 0):
#     global minval
#     if k == n:
#         if temp > maxval:
#             maxval = temp
#     else:
#         for i in range(k, n):
#             arr[k], arr[i] = arr[i], arr[k]
#             if sum + temp * P[k][arr[k]]/100 > maxval:
#                 perm(k + 1, temp * P[k][arr[k]]/100)
#             arr[k], arr[i] = arr[i], arr[k]

import itertools

T = int(input())
for tc in range(T):
    N = int(input())
    NN = [list(map(int, input().split())) for _ in range(N)]
    arr = [i for i in range(1, N+1)]
    minval = 1000000
    subset = list(itertools.permutations(arr))
    for i in subset:
        temp = NN[0][i[0]]
        flag = 0
        for j in range(N-2):
            if temp + NN[i[j]][i[j+1]] < minval:
                flag = 1
                break
            else:
                temp += NN[i[j]][i[j+1]]
        if not flag and temp + NN[i[-1]][0] < minval:
            minval = temp + NN[i[-1]][0]
    print('#%d %d' % (tc, minval))


    # print("#%d %f" % (tc + 1, round(maxval, 6)))
