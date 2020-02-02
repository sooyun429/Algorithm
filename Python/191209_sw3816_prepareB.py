import sys
sys.stdin = open('sw3816.txt', 'r')

for tc in range(1, int(input())+1):
    S1, S2 = map(str, input().split())
    res = 0
    N, M = len(S1), len(S2)
    if N <= M:
        for i in range(M-N+1):
            temp = S1
            for j in range(N):
                if S2[i+j] not in temp:
                    break
                else:
                    index = temp.index(S2[i+j])
                    temp = temp[:index] + temp[index+1:]
            else:
                res += 1
    print("#%d %d" % (tc, res))


# ## 시간을 더 단축시켜야 함
# for tc in range(1, int(input())+1):
#     S1, S2 = map(str, input().split())
#     res = 0
#     N, M = len(S1), len(S2)
#     if N <= M:
#         for i in range(M-N+1):
#             for j in range(N):
#                 if S2[i+j] not in S1:
#                     break
#                 elif S2[i:i+N].count(S2[i+j]) != S1.count(S2[i+j]):
#                     break
#             else:
#                 res += 1
#     print("#%d %d" % (tc, res))




# ## itertools를 쓰면 제한시간 초과가 나기 쉽다.. 다른 방법 생각해보자
# import itertools
#
# for tc in range(1, int(input())+1):
#     S1, S2 = map(str, input().split())
#     res = 0
#     N, M = len(S1), len(S2)
#     if N <= M:
#         S1 = list(set(itertools.permutations(list(S1))))
#         for i in S1:
#             word = ''.join(i)
#             for j in range(M-N+1):
#                 if S2[j:j+N] == word:
#                     res += 1
#     print("#%d %d" % (tc, res))
