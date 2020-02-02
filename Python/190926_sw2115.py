import sys
sys.stdin = open('sw2115.txt', 'r')


def findmax(arr, maxsum):
    if sum(arr) > C:
        for k in range(len(arr)):
            if arr[:k] < C and sum(arr[:k]) > maxsum:
                maxsum = sum(arr[:k])
            if arr[k:] < C and sum(arr[k:]) > maxsum:
                maxsum = sum(arr[k:])
    else:
        if sum(arr) > maxsum:
            maxsum = sum(arr)


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    NN = [list(map(int, input().split())) for _ in range(N)]
    Amaxsum = Bmaxsum = 0
    for i in range(N):
        for j in range(N-M+1):
            findmax(NN[i][j:j + M + 1], Amaxsum)  # A의 최대sum값 찾기
            Atemp =
            Amaxsum = 0



            Bmaxsum = 0
            if j+M*2 < N:
                for k in [j+M+1:j+M*2+1]:
                    temp2 = NN[i][k:k+M+1]

