import sys
sys.stdin = open('sw5202.txt', 'r')


# def perm(k, n):
#     global p
#     if k == n:
#         # if
#         print(arr)
#
#         return arr
#     else:
#         for i in range(k, n):
#             if truck[i][1] <= truck[k][0]:
#                 arr[k], arr[i] = arr[i], arr[k]
#                 perm(k+1, n)
#                 arr[k], arr[i] = arr[i], arr[k]


def perm(o, u):



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    truck = sorted([list(map(int, input().split())) for _ in range(N)])
    print(truck)
    # arr = [i for i in range(N)]
    # p = []
    # for i in range(N, -1, -1):
    #     perm(0, i)
    flag = 0
    for i in range(len(truck)):
        used = [0] * N
        for j in range(i):
            if truck[i][0] >= truck[j][1]:
                flag = 1
        if flag:
            break
        else:
            order = [truck[i]]
            used[i] = 1
            perm(order, used)
        perm(i)



