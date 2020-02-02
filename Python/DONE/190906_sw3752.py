import sys
sys.stdin = open('sw3752.txt', 'r')

# # set 활용(설유언니 코드 참고)
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     results = {0}
#     for i in scores:
#         for j in list(results):
#             results.add(i + j)
#     print('#%d %d' % (tc, len(results)))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    results = [0]
    for i in scores:
        for j in range(len(results)):
            results.append(i + results[j])
        results = list(set(results))  # 중간마다 results의 중복값 제거해서 메모리초과 에러 해결
    res = len(set(results))
    print('#%d %d' % (tc, res))

#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     results = {0} + {scores[0]}
#     for i in scores[1:]:
#         temp = {results[j] + i for j in range(len(results))}
#         results += temp
#     print('#%d %d' % (tc, len(set(results))))




# 런타임에러 수정 실패
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     n = len(scores)
#     cases = []
#
#     for i in range(1 << n):
#         temp = [0]*n
#         for j in range(n+1):
#             if i & (1 << j):
#                 temp[j] = scores[j]
#         if sum(temp) not in cases:
#             cases.append(sum(temp))
#     print('#%d %d' % (tc, len(cases)))

# # 비트연산 활용한 방법 (배열 2 수업자료에 있음)
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     n = len(scores)
#     cases = [0]*(2**n)
#
#     for i in range(1<<n):
#         temp = []
#         for j in range(n+1):
#             if i & (1<<j):
#                 temp.append(scores[j])
#         cases[i] = temp
#     # print(cases)
#     result = []
#     for i in range(len(cases)):
#         if sum(cases[i]) not in result:
#             result.append(sum(cases[i]))
#     print('#%d %d' % (tc, len(result)))
