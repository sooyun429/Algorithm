import sys
sys.stdin = open('sw5247.txt', 'r')

## visited 체크하는 방식 - 제한시간 초과
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    calnums = {N}
    cnt = 0
    A = (M+10)//2
    visited = [0] * 1000000
    while True:
        cnt += 1
        flag = 0
        for i in list(calnums):
            if visited[i] == 0:
                visited[i] = 1
                lst = [i+1, i-1, i*2, i-10]
                temp = []
                if M in lst:
                    flag = 1
                    break
                if i <= M+9:
                    temp += [lst[0]]
                if i <= A:
                    temp += [lst[2]]
                if i-10 > 0:
                    temp += [lst[3], lst[1]]
                elif i-1 > 0:
                    temp += [lst[1]]
                calnums.update(set(temp))
        if flag:
            break
    print('#%d %d' % (tc, cnt))


# ## 제한시간 초과
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     calnums = {N}
#     cnt = 0
#     A = (M+10)//2
#     while True:
#         cnt += 1
#         flag = 0
#         for i in list(calnums):
#             if M in [i+1, i-1, i*2, i-10]:
#                 flag = 1
#                 break
#             if i <= M+9:
#                 calnums.add(i+1)
#             if i-1 > 0:
#                 calnums.add(i-1)
#             if i <= A:
#                 calnums.add(i*2)
#             if i-10 > 0:
#                 calnums.add(i-10)
#         if flag:
#             break
#     print('#%d %d' % (tc, cnt))


## 제한시간 초과~~
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     calnums = {N}
#     cnt = 0
#     A = (M+10)//2
#     while True:
#         temp = set()
#         for i in list(calnums):
#             if i+1 not in calnums and i <= M+9:
#                 temp.add(i+1)
#             if (i-1 not in calnums) and i-1 > 0:
#                 temp.add(i-1)
#             if (i*2 not in calnums) and i <= A:
#                 temp.add(i*2)
#             if (i-10 not in calnums) and i-10 > 0:
#                 temp.add(i-10)
#         cnt += 1
#         if M in list(temp):
#             break
#         calnums.update(temp)
#     print('#%d %d' % (tc, cnt))


# ## 제한시간 초과
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     calnums = {N}
#     cnt = 0
#     A = (M+10)//2
#     while True:
#         temp = []
#         for i in list(calnums):
#             if i <= A:
#                 if i > 10:
#                     temp += [i+1, i-1, i*2, i-10]
#                 else:
#                     if i > 1:
#                         temp += [i + 1, i - 1, i * 2]
#                     else:
#                         temp += [i + 1, i * 2]
#             else:
#                 if i > 10:
#                     temp += [i+1, i-1, i-10]
#                 else:
#                     if i > 1:
#                         temp += [i + 1, i - 1]
#                     else:
#                         temp += [i + 1]
#         cnt += 1
#         temp = set(temp)
#         if M in list(temp):
#             break
#         calnums.update(temp)
#     print('#%d %d' % (tc, cnt))


# # 제한시간 초과
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     calnums = [N]
#     cnt = 0
#     while M not in calnums:
#         temp = []
#         for i in calnums:
#             if i*2 <= M+10:
#                 if i-10 > 0:
#                     temp += [i+1, i-1, i*2, i-10]
#                 else:
#                     if i-1 > 0:
#                         temp += [i + 1, i - 1, i * 2]
#                     else:
#                         temp += [i + 1, i * 2]
#             else:
#                 if i - 10 > 0:
#                     temp += [i+1, i-1, i-10]
#                 else:
#                     if i-1 > 0:
#                         temp += [i + 1, i - 1]
#                     else:
#                         temp += [i + 1]
#         cnt += 1
#         calnums += temp
#         calnums = list(set(calnums))
#     print('#%d %d' % (tc, cnt))

# # runtime error
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     calnums = [N]
#     cnt = 0
#     while M not in calnums:
#         temp = []
#         for i in calnums:
#             temp += [i+1, i-1, i*2, i-10]
#         cnt += 1
#         calnums += temp
#         calnums = list(set(calnums))
#     print('#%d %d' % (tc, cnt))
