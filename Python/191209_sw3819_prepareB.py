import sys
sys.stdin = open('sw3819.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [0 for _ in range(N)]
    sum_arr = [0 for _ in range(N)]
    res = 0
    minnum = 0
    maxnum = 0
    for n in range(N):
        arr[n] = int(input()) # arr에 각 데이터 입력
        if n==0:  # n이 0인 경우 이전 sum값이 없으므로 별도처리
            sum_arr[n] = arr[n]
        else:  # sum_arr에 index n번째 까지의 sum값 저장
            sum_arr[n] = sum_arr[n - 1] + arr[n]
            if sum_arr[n-1] < minnum:
                minnum = sum_arr[n-1]
        if sum_arr[n]-minnum > maxnum:
            maxnum = sum_arr[n]-minnum
    print("#%d %d" % (tc, maxnum))


# ## 런타임에러
# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [0 for _ in range(N)]
#     res = 0
#     for n in range(N):
#         arr[n] = int(input())
#     for i in range(N):
#         for j in range(i, N):
#             temp = sum(arr[i:j+1])
#             # print(arr[i:j+1])
#             if temp > res:
#                 res = temp
#                 # print(res)
#     print("#%d %d" % (tc, res))
