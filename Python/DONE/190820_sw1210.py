import sys
sys.stdin = open('sw1210_input.txt', 'r')

for _ in range(10):
    T = input()
    L = [input().split() for _ in range(100)]  # Ladder
    r = 99
    c = L[r].index('2') # Destination 인덱스값(column)
    idx = []

    for index in range(100):  # 사다리 세로줄 있는 인덱스 (0번째 row에서 확인)
        if L[0][index] == '1':
            idx.append(index)

    while r:
        if c == 0:
            if L[r][c + 1] == '1':
                c = idx[idx.index(c) + 1]
        elif c == 99:
            if L[r][c - 1] == '1':
                c = idx[idx.index(c) - 1]
        else:
            if L[r][c + 1] == '1':
                c = idx[idx.index(c) + 1]
            elif L[r][c - 1] == '1':
                c = idx[idx.index(c) - 1]
        r -= 1
    print('#%s %d' % (T, c))
