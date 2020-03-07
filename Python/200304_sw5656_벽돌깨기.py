import sys
sys.stdin = open('sw5656.txt', 'r')

def breakbricks(x, y, arr, cnt):
    # print(arr, cnt)
    if x < W & x >= 0 & y < H & y >= 0:
        if arr[y][x]:
            length = arr[y][x]
            for i in range(length-1, 0, -1):
                breakbricks(x+i, y, arr, cnt)
                # print(arr, cnt)
                breakbricks(x-i, y, arr, cnt)
                # print(arr, cnt)
                breakbricks(x, y+i, arr, cnt)
                breakbricks(x, y-i, arr, cnt)
            arr[y][x] = 0
            cnt += 1
            return [arr, cnt]
    return 0

for tc in range(1, int(input())+1):
    # 정보 가져오기
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    # for i in arr: print(i)

    for _ in range(N):
        maxres = 0
        for x in range(W):
            for y in range(H):
                temp = breakbricks(x, y, arr, 0)
                print(temp)
                if temp:
                    if maxres < temp[1]:
                        maxres = temp[1]
                        arr = temp[0]
                        for i in range(W-1, 1, -1):
                            for j in range(H-1, 1, -1):
                                if arr[j][i] == 0:
                                    for k in range(j-1, -1, -1):
                                        if arr[k][i]:
                                            arr[j][i], arr[k][i] = arr[k][i], arr[j][i]
                                            break

    # res = 0
    # for x in range(W):
    #     for y in range(H):
    #         print(arr, x, y, W, H)
    #         if arr[y][x]:
    #             res += 1

    # print('#%d %d' % (tc, res))
