import sys
sys.stdin = open('sw4861_input.txt', 'r')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    NN = [0] * N
    result = ''
    for i in range(N):
        NN[i] = input()
    for i in range(N):
        for j in range(0, N - M + 1):
            str1 = NN[i][j:j+M]
            str2 = list(str1)
            str2.reverse()
            if str1 == ''.join(str2):
                result = str1
                break
        if result:
            break
    NN2 = [''] * N
    if result == '':
        for i in range(N):
            for j in range(N):
                NN2[i] += NN[j][i]
            for k in range(0, N - M + 1):
                str1 = NN2[i][k:k+M]
                str2 = list(str1)
                str2.reverse()
                if str1 == ''.join(str2):
                    result = str1
                    break
            if result: break
    print('#%d %s' % (tc + 1, result))
