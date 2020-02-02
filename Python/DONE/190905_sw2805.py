import sys
sys.stdin = open('sw2805.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    land = [list(map(int, input())) for _ in range(N)]
    result = 0
    idx = N//2  # 더해야 하는 숫자 시작 위치 인덱스값 위쪽만 (2, 1, 0)
    row1 = 0  # 위쪽 row 인덱스값(0, 1, ... , N//2까지)
    row2 = -1  # 아래쪽 row 인덱스값(-1, -2..., -(N//2)까지)

    for i in range(1, N, 2):  # 한 줄에 더해야 하는 갯수 (1, 3, 5, 7, ...)
        result += sum(land[row1][idx:idx+i]) + sum(land[row2][idx:idx+i])
        idx -= 1
        row1 += 1
        row2 -= 1
    result += sum(land[row1])

    print('#%d %d' % (tc, result))
