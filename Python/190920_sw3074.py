import sys
sys.stdin = open('sw3074.txt', 'r')

def binary(s, e, flag):
    global timedata, result
    m = (s+e)//2
    temp = 0
    for i in timedata:
        temp += m//i
    print(s, e, m, temp)
    if temp == M:
        result = m
        print('11111')
        return
    elif temp > M:
        if flag == 0:
            result = s-1
            print('2222')
            return
        else:
            print('3333')
            binary(s, m-1, 1)
    # elif temp > M:
    #     print('11111', s, m-1)
    #     binary(s, m-1)
    else:
        if flag:
            print('4444')
            result = e+1
            return
        else:
            print('5555')
            binary(m+1, e, 0)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    timedata = [int(input()) for _ in range(N)]
    mintime = min(timedata)
    binary(1, mintime * M, 0)
    # print(result)
    print('#%d %d' % (tc, result))

# # 제한시간 초과
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     timedata = [int(input()) for _ in range(N)]
#     mintime = min(timedata)
#     for i in range(mintime*M, -1,-1):
#         temp = 0
#         for j in timedata:
#             temp += i//j
#         if temp < M:
#             result = i + 1
#             break
#     print('#%d %d' % (tc, result))


# # runtime error
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     timedata = [int(input()) for _ in range(N)]
#     lst = [0]*N*M
#     idx = 0
#     for i in range(N):
#         for j in range(1, M+1):
#             lst[idx] = timedata[i]*j
#             idx += 1
#     lst.sort()
#     print('#%d %d' % (tc, lst[M-1]))


## 제한시간 초과(세 번째 시도)
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     timedata = [int(input()) for _ in range(N)]
#     maxidx = timedata.index(max(timedata))
#     cnt = [1]*N
#     while sum(cnt) <= M:
#         temp = timedata[maxidx]*cnt[maxidx]
#         # print(timedata[:-1])
#         # print(order)
#         for i in range(len(timedata)):
#             while timedata[i]*cnt[i] <= temp:
#                 cnt[i] += 1
#                 # print(order, cnt)
#         cnt[maxidx] += 1
#     order = [0] * sum(cnt)
#     idx = 0
#     for i in range(len(timedata)):
#         for j in range(1, cnt[i]+1):
#             order[idx] = timedata[i]*j
#             idx += 1
#     order.sort()
#     print('#%d %d' % (tc, order[M-1]))


# ## 제한시간 초과 (두 번째 시도)
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     timedata = [int(input()) for _ in range(N)]
#     timedata.sort()
#     mintime = timedata[0]
#     counter = [0]*N
#     second = mintime
#     flag = 0
#     while M:
#         second += mintime
#         for i in range(len(counter)):
#             while counter[i] <= second:
#                 counter[i] += timedata[i]
#                 M -= 1
#                 # print(timedata)
#                 # print(counter, second, M)
#                 if M == 0:
#                     flag = 1
#                     break
#             if flag:
#                 break
#     print('#%d %d' % (tc, max(counter)))


# # runtime error (첫 번째 시도)
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     timedata = [int(input()) for _ in range(N)]
#     maxtime = max(timedata)
#     counter = [0] * (maxtime+1)
#     for i in range(1, maxtime+1):
#         counter[i] = timedata.count(i)
#     second = 0
#     flag = 0
#     while True:
#         second += 1
#         for i in range(len(counter)):
#             if counter[i] and (second % i == 0):
#                 M -= counter[i]
#                 if M <= 0:
#                     flag = 1
#                     break
#         if flag:
#             break
#     print('#%d %d' % (tc, second))
