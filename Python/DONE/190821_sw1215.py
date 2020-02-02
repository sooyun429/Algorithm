import sys
sys.stdin = open('sw1215_input.txt', 'r')

for tc in range(10):
    M = int(input())
    NN = [0] * 8
    result = 0
    for i in range(8):
        NN[i] = input()

    for i in range(8):
        for j in range(0, 8 - M + 1):
            str1 = NN[i][j:j + M]
            str2 = list(str1)
            str2.reverse()
            if str1 == ''.join(str2):
                result += 1

    NN2 = [''] * 8
    for i in range(8):
        for j in range(8):
            NN2[i] += NN[j][i]
        for k in range(0, 8 - M + 1):
            str1 = NN2[i][k:k + M]
            str2 = list(str1)
            str2.reverse()
            if str1 == ''.join(str2):
                result += 1

    print('#%d %s' % (tc + 1, result))