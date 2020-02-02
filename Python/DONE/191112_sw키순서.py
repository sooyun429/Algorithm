import sys, copy
sys.stdin = open('sw키순서.txt', 'r')

# ## 시간초과 나고 통과 못함
# def ordercnt(bigsmall, idx):
#     global cnt, temp
#     if infos[idx][bigsmall]:
#         for j in infos[idx][bigsmall]:
#             if cnt[bigsmall][j] == 0:
#                 cnt[bigsmall][j] = 1
#                 temp += 1
#             ordercnt(bigsmall, j)
#     else:
#         return
#
#
# # 입력값 받아오기
# for tc in range(1, int(input())+1):
#     N, M = int(input()), int(input())
#     infos = [[[] for _ in range(2)] for _ in range(N+1)]
#     for _ in range(M):
#         a, b = map(int, input().split())
#         infos[a][1] += [b]
#         infos[b][0] += [a]
#     # print(infos)
# # 키 정보(작은 번호 cnt, 큰 번호 cnt)
#     res = 0
#     for i in range(1, N+1):
#         temp = 0
#         cnt = [[0 for _ in range(N+1)] for _ in range(2)]
#         ordercnt(0, i)
#         ordercnt(1, i)
#         if temp == N-1:
#             res += 1
#     print('#%d %d' % (tc, res))


## set과 deepcopy를 사용함
# 입력값 받아오기
for tc in range(1, int(input())+1):
    N, M = int(input()), int(input())
    infos = [[set() for _ in range(2)] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        infos[a][1].add(b)
        infos[b][0].add(a)
    # print(infos)
# 키 정보(작은 번호 0, 큰 번호 1) 입력
    while True:
        compare = copy.deepcopy(infos)
        for i in range(1, N+1):
            for j in list(infos[i][0]):
                infos[i][0].update(infos[j][0])
            for j in list(infos[i][1]):
                infos[i][1].update(infos[j][1])
        if compare == infos: break
    # print(infos)
    cnt = 0
    for info in infos:
        if len(info[0])+len(info[1])+1 == N:
           cnt +=1
    print('#%d %d' % (tc, cnt))




# ## deepcopy 대신 flag 사용(역시 제한시간 초과)
# # 입력값 받아오기
# T = int(input())
# for tc in range(1, T+1):
#     N, M = int(input()), int(input())
#     infos = [[[] for _ in range(2)] for _ in range(N+1)]
#     for _ in range(M):
#         a, b = map(int, input().split())
#         infos[a][1].append(b)
#         infos[b][0].append(a)
#     # print(infos)
# # 키 정보(작은 번호 0, 큰 번호 1) 입력
#     while True:
#         flag = 1
#         for i in range(1, N+1):
#             for j in infos[i][0]:
#                 for k in infos[j][0]:
#                     if k not in infos[i][0]:
#                         infos[i][0].append(k)
#                         flag = 0
#             for j in infos[i][1]:
#                 for k in infos[j][1]:
#                     if k not in infos[i][1]:
#                         infos[i][1].append(k)
#                         flag = 0
#         if flag: break
#     # print(infos)
#     cnt = 0
#     for info in infos:
#         if len(info[0])+len(info[1])+1 == N:
#            cnt +=1
#     print('#%d %d' % (tc, cnt))



# ## deepcopy 사용(제한시간 초과)
# import copy
#
# # 입력값 받아오기
# T = int(input())
# for tc in range(1, T+1):
#     N, M = int(input()), int(input())
#     infos = [[[] for _ in range(2)] for _ in range(N+1)]
#     for _ in range(M):
#         a, b = map(int, input().split())
#         infos[a][1].append(b)
#         infos[b][0].append(a)
#     # print(infos)
# # 키 정보(작은 번호 0, 큰 번호 1) 입력
#     while True:
#         compare = copy.deepcopy(infos)
#         for i in range(1, N+1):
#             for j in infos[i][0]:
#                 for k in infos[j][0]:
#                     if k not in infos[i][0]: infos[i][0].append(k)
#             for j in infos[i][1]:
#                 for k in infos[j][1]:
#                     if k not in infos[i][1]: infos[i][1].append(k)
#         if infos == compare: break
#     # print(infos)
#     cnt = 0
#     for info in infos:
#         if len(info[0])+len(info[1])+1 == N:
#            cnt +=1
#     print('#%d %d' % (tc, cnt))

