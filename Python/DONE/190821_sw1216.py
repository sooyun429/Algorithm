import sys
sys.stdin = open('sw1216_input.txt', 'r')
#
# for tc in range(10):
#     T = int(input())
#     NN = [0] * 100
#     result = 0
#     for i in range(100):
#         NN[i] = input()
#
#     for i in range(100):
#         for j in range(100):
#             for k in range(0,  100 - j + 1):
#                 str1 = NN[i][k:k + j]
#                 str2 = list(str1)
#                 str2.reverse()
#                 if str1 == ''.join(str2):
#                     if result < len(str1):
#                         result = len(str1)
#
#     NN2 = [''] * 100
#     for i in range(100):
#         for j in range(100):
#             NN2[i] += NN[j][i]
#         for j in range(100):
#             for k in range(0, 100 - j + 1):
#                 str1 = NN2[i][k:k + j]
#                 str2 = list(str1)
#                 str2.reverse()
#                 if str1 == ''.join(str2):
#                     if result < len(str1):
#                         result = len(str1)
#
#     print('#%d %s' % (tc + 1, result))


    # ['C', 'CC', 'BCB', 'CBBC', 'BCCCB', 'CBAABC', 'ABCCCBA', 'AACBCBCAA', 'CCBBAABBCC',
    # 'AABBBCBBBAA', 'CACCBCCCBCCAC',
    #  'ACBBAABBAABBCA', 'BCCACBCACBCACCB', 'ABCCACBCACBCACCBA', 'ABAAACABAABACAAABA']

# ## 더 간략화
# for tc in range(10):
#     T = int(input())
#     NN = [0] * 100
#     result = result2 = 0
#     for i in range(100):
#         NN[i] = input()
#
#     for j in range(100, 0, -1):
#         for i in range(100):
#             for k in range(0,  100 - j + 1):
#                 str1 = NN[i][k:k + j]
#                 str2 = list(str1)
#                 str2.reverse()
#                 if str1 == ''.join(str2):
#                     result = len(str1)
#                     break
#             if result: break
#         if result: break
#
#     NN2 = [''] * 100
#     for i in range(100):
#         for j in range(100):
#             NN2[i] += NN[j][i]
#
#     for j in range(100, 0, -1):
#         for i in range(100):
#             for k in range(0, 100 - j + 1):
#                 str1 = NN2[i][k:k + j]
#                 str2 = list(str1)
#                 str2.reverse()
#                 if str1 == ''.join(str2):
#                     result2 = len(str1)
#                     break
#             if result2:
#                 break
#         if result2:
#             break
#     if result2 > result:
#         result = result2
#     print('#%d %s' % (tc + 1, result))


## 다른 방법(2차원 배열을 바꾸지 않고)??

for tc in range(10):
    T = int(input())
    NN = [0] * 100
    result = 0
    for i in range(100):
        NN[i] = input()

    for i in range(100, 0, -1):  # 회문의 길이
        for j in range(100):
            for s in range(0, 100 - i + 1):  # 시작지점
                k = k2 = 0
                stack = []
                stack2 = []
                while k < i // 2:
                    stack.append(NN[j][s+k])
                    stack2.append(NN[s+k2][j])
                    k += 1
                    k2 += 1

                if i % 2:
                    k += 1
                    k2 += 1

                while NN[j][s+k] == stack[-1]:
                    stack.pop()
                    if len(stack) == 0:
                        result = i
                        break
                    k += 1
                if result: break

                while NN[s+k2][j] == stack2[-1]:
                    stack2.pop()
                    if len(stack2) == 0:
                        result = i
                        break
                    k2 += 1
                if result: break
            if result: break
        if result: break

    print('#%d %s' % (tc + 1, result))
