import sys
sys.stdin = open('sw5110.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = [0, 0]*N
    temp = list(map(int, input().split()))
    for i in range(temp):
        result[i][1] = temp[i]
    for i in range(M-1):
        temp = list(map(int, input().split()))
        for j in range(temp):
            temp[j] = [0, temp[j]]
        for j in range(result):
            if result[j][1] > temp[0][1]:
                result[j-1][0] = temp
        # result 값을 모두 확인했는데 temp 1번째 값보다 모두 작은 경우 temp를 result 뒤에 붙여준다.
        if result[j][1] < temp[0][1]:
            result = result + temp
    cnt = 1
    reverse = -1
    while cnt != 10:




#
#
#
# # 첫 번째 시도 (제한시간 초과 Fail)
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     result = list(map(int, input().split()))
#     for i in range(M-1):
#         li = list(map(int, input().split()))
#         temp = len(result)
#         for j in range(len(result)):
#             if result[j] > li[0]:
#                 result = result[:j] + li + result[j:]
#                 break
#         if len(result) == temp:
#             result += li
#     numbers = ''
#     if len(result) > 10:
#         for i in result[-1:-11:-1]:
#             numbers += ' ' + str(i)
#     else:
#         for i in result[::-1]:
#             numbers += ' ' + str(i)
#     print('#%d%s' % (tc, numbers))
