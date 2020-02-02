import sys
sys.stdin = open('sw3408_input.txt', 'r')

# T = int(input())
# for tc in range(T):
#     N = int(input())
#     S1 = S2 = S3 = 0
#     for i in range(1, N+1):
#         S1 += i
#         S2 += 2*i-1
#         S3 += 2*i
#     print('#%d %d %d %d' % (tc+1, S1, S2, S3))


T = int(input())
for tc in range(T):
    N = int(input())
    S1 = (1+N)*N//2  # int 타입 단순히 /로 나누면 float타입으로 바뀌면서 답이 틀리게 됨
    S2 = N**2
    S3 = S1*2
    print('#%d %d %d %d' % (tc+1, S1, S2, S3))