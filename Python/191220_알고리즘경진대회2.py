import sys
sys.stdin = open('12.txt', 'r')

import itertools

for tc in range(1, int(input()) + 1):
    N, x, y = map(int, input().split())
    temp = list(str(N))
    length = len(temp)
    if x > y: x, y = y, x
    for i in range(length, 0, -1):
        candidate = list(set(itertools.permutations([x for _ in range(i)]+[y for _ in range(i)], i)))
        candidate.sort(reverse=True)
        res = 0
        # print(candidate)
        for j in candidate:
            # print(j)
            num = 0
            for k in range(i):
                # print(k)
                num += j[-1-k]*(10**k)
            # print(num)
            if num < N:
                res = num
                break
        if res:
            break
    if res == 0:
        res = -1
    print("#%d %d" % (tc, res))

# 4
# 16 1 3  # 1 13
# 2 6 9  # 2 -1
# 5 0 8  # 3 -1
# 422223324 2 4  # 4 422222444