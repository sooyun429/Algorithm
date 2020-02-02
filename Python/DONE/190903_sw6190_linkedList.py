import sys
sys.stdin = open('sw6190.txt', 'r')

# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     result = -1
#     for i in range(N):
#         for j in numbers[i+1:]:
#             x = numbers[i]*j
#             str_x = list(str(x))
#             cnt = 1
#             for k in range(len(str_x)-1):
#                 if str_x[k] > str_x[k+1]:
#                     cnt = 0
#                     break
#             if cnt == 1 and x > result:
#                 result = x
#     print('#%d %d' % (tc, result))


## 아래처럼 순서 바꿀 수 있음(최대값 체크 먼저)
## 곱한 값이 max(최대값)보다 큰 지 여부를 먼저 체크하면 더 짧게 줄일 수 있다.

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = -1
    for i in range(N):
        for j in numbers[i+1:]:
            x = numbers[i]*j
            if x > result:
                str_x = list(str(x))
                cnt = 1
                for k in range(len(str_x)-1):
                    if str_x[k] > str_x[k+1]:
                        cnt = 0
                        break
                if cnt == 1:
                    result = x
    print('#%d %d' % (tc, result))
