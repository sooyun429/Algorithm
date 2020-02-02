import sys
sys.stdin = open('sw1979.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    NN = [[0]*(N+2)] + [([0] + list(map(int, input().split())) + [0]) for _ in range(N)] + [[0]*(N+2)]
    # for i in NN:
    #     print(i, end = '\n')
    result = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            cnt_h = cnt_v = 0  # horizontal 가로 vertical 세로 길이 카운트
            if NN[i][j]:
                if NN[i][j-1] == 0:  # 가로 카운트는 1이 처음 시작할 때만 적용
                    for k in range(j, N+1):
                        cnt_h += 1
                        if NN[i][k+1] == 0:
                            break
                    if cnt_h == K:
                        result += 1
                if NN[i-1][j] == 0:  # 세로 카운트는 위 칸이 0이면서 아래칸도 1일 때마다 적용해서 체크
                    for k in range(i, N+1):
                        cnt_v += 1
                        if NN[k+1][j] == 0:
                            break
                    if cnt_v == K:
                        result += 1
    print('#%d %d' % (tc, result))
