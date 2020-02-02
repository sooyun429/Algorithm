import sys, itertools
sys.stdin = open('sw1247.txt', 'r')


## itertools 사용하지 않고 순열 만드는 방법 익히기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    temp = list(map(int, input().split()))
    temp = temp[:2] + temp[4:] + temp[2:4]
    location = [0]*(len(temp)//2)
    for i in range(0, len(temp), 2):
        location[i//2] = [temp[i], temp[i+1]]
    customers = [i+1 for i in range(N)]
    comb = itertools.permutations(customers)
    minlength = sum(temp)*2
    distance = [[0]*(N*2) for _ in range(N+2)]
    for i in range(len(location)-1):
        for j in range(i+1, len(location)):
            distance[i][j] = distance[j][i] = abs(location[i][0]-location[j][0]) + abs(location[i][1] - location[j][1])
    for i in comb:
        orders = [0] + list(i) + [N+1]
        add = 0
        for j in range(len(orders)-1):
            add += distance[orders[j]][orders[j+1]]
        if add < minlength:
            minlength = add
    print('#%d %d' % (tc, minlength))


## 실패
# def perm(a):
#     global minlength, distance
#     if len(a) == 1:
#         return [a]
#     else:
#         result = []
#         for i in a:
#             b = a.copy()
#             b.remove(i)
#             b.sort()
#             for j in perm(b):
#                 j.insert(0, i)
#                 if j not in result:
#                     result.append(j)
#         if len(result) == N:
#             result = [0] + result + [N+1]
#             print(result)
#             temp = 0
#             for k in range(len(result)-1):
#                 temp += distance[k][k+1]
#             if temp < minlength:
#                 minlength = temp
#     return result
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     temp = list(map(int, input().split()))
#     temp = temp[:2] + temp[4:] + temp[2:4]
#     location = [0]*(len(temp)//2)
#     for i in range(0, len(temp), 2):
#         location[i//2] = [temp[i], temp[i+1]]
#     distance = [[0]*(N+2) for _ in range(N+2)]
#     for i in range(len(location)):
#         for j in range(i+1, len(location)):
#             distance[i][j] = distance[j][i] = abs(location[i][0] - location[j][0]) + abs(location[i][1] - location[j][1])
#
#     customers = [i+1 for i in range(N)]
#     print(customers)
#     minlength = sum(temp)*2
#     perm(customers)
#     print('#%d %d' % (tc, minlength))
#


## 첫 번째 시도
# def perm(a):
#     if len(a) == 1:
#         return[a]
#     else:
#         result = []
#         for i in a:
#             b = a.copy()
#             b.remove(i)
#             b.sort()
#             for j in perm(b):
#                 j.insert(0, i)
#                 if j not in result:
#                     result.append(j)
#     return result
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     temp = list(map(int, input().split()))
#     temp = temp[:2] + temp[4:] + temp[2:4]
#     location = [0]*(len(temp)//2)
#     for i in range(0, len(temp), 2):
#         location[i//2] = [temp[i], temp[i+1]]
#     customers = [i+1 for i in range(N)]
#     orders = perm(customers)
#     minlength = sum(temp)*2
#     for i in orders:
#         cal = abs(location[0][0]-location[i[0]][0]) + abs(location[0][1]-location[i[0]][1])
#         for j in range(1, len(i)):
#             cal += abs(location[i[j-1]][0]-location[i[j]][0]) + abs(location[i[j-1]][1]-location[i[j]][1])
#         cal += abs(location[i[-1]][0]-location[-1][0]) + abs(location[i[-1]][1]-location[-1][1])
#         if minlength > cal:
#             minlength = cal
#     print('#%d %d' % (tc, minlength))
