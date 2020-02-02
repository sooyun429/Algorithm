import sys
sys.stdin = open('sw1240.txt', 'r')

T = int(input())
scanner = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
for tc in range(1, T+1):
    N, M = map(int, input().split())
    NN = [list(input()) for _ in range(N)]
    for i in range(len(NN)-1, -1, -1):
        idx = M-1
        code = [0]*8
        cnt = 7
        while idx > 5 and cnt > -1:
            if NN[i][idx] == '1' and (''.join(NN[i][idx-6:idx+1]) in scanner):
                code[cnt] = scanner.index(''.join(NN[i][idx-6:idx+1]))
                cnt -= 1
                idx -= 6
            idx -= 1
        if cnt < 0:
            break
    result = 0
    even = sum(code[0::2])
    odd = sum(code[1::2])
    if (even*3 + odd) % 10:
        result = 0
    else:
        result = even + odd

    print('#%d %d' % (tc, result))
