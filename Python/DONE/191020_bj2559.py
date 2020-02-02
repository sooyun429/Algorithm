import sys
sys.stdin = open('bj2559.txt', 'r')

N, K = map(int, input().split())
T = list(map(int, input().split()))
temp = sum(T[0:K])
result = temp
for i in range(N-K):
    temp = temp - T[i] + T[i+K]
    if temp > result:
        result = temp
print(result)


# # 시간 초과
# N, K = map(int, input().split())
# T = list(map(int, input().split()))
# result = sum(T[0:K])
# for i in range(1, N-K+1):
#     if T[i-1] < T[i+K-1]:
#         temp = sum(T[i:i+K])
#         if temp > result:
#             result = temp
# print(result)
