import sys
sys.stdin = open('sw4299.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    D, H, M = map(int, input().split())
    if D == 11:

    result = (nowtime-appointment).seconds
    if result < 0:
        result = -1
    print('#%d %d' % (tc, result))


# ## 왜 에러가 나는 것인가..
# from datetime import datetime, timedelta
# T = int(input())
# for tc in range(1, T+1):
#     D, H, M = map(int, input().split())
#     appointment = datetime(2011, 11, 11, 11, 11, 0)
#     nowtime = datetime(2011, 11, D, H, M, 0)
#     print(appointment, nowtime)
#     result = (nowtime-appointment).seconds
#     if result < 0:
#         result = -1
#     print('#%d %d' % (tc, result))
