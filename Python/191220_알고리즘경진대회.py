import sys
sys.stdin = open('12.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, x, y = map(int, input().split())
    arr = list(str(N))
    length = len(arr)
    if x > y: x, y = y, x
    res = [0 for _ in range(length)]
    for index in range(length):
        n = int(N[index])

        if n >= x:
            if n >= y:
                res[index] = y
            else:
                res = x

        else:
            for j in range(index, -1, -1):

            res = 0
            for i in range(length-1):
                res += y*(10**i)

    print("#%d %d" % (tc, res))

# 4
# 16 1 3  # 1 13
# 2 6 9  # 2 -1
# 5 0 8  # 3 -1
# 422223324 2 4  # 4 422222444
