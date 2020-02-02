import sys
sys.stdin = open('sw4047.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    cardtype = ['S', 'D', 'H', 'C']
    cardset = [[0]*14 for _ in range(4)]
    S = input()
    temp = [13] * 4
    result = 0
    for i in range(len(S)):
        if S[i] in cardtype:
            idx = cardtype.index(S[i])
            num = int(S[i+1:i+3])
            if cardset[idx][num] == 1:
                result = 'ERROR'
                break
            else:
                cardset[idx][num] += 1
                temp[idx] -= 1
    if result != 'ERROR':
        result = '%d %d %d %d' % (temp[0], temp[1], temp[2], temp[3])
    print('#%d %s' % (tc, result))
