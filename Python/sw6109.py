import sys
sys.stdin = open('sw6109.txt', 'r')
##### up만 만족시킴 다른 방향도 고민해봐야 함
T = int(input())
direction = ['left', 'right', 'up', 'down']
dx = [1, -1, 0, 0]  # 이동 방향이므로 확인하는 좌표는 반대(-)로 확인할 예정
dy = [0, 0, -1, 1]

for tc in range(1, T+1):
    N, D = map(str, input().split())
    N = int(N)
    NN = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        print(NN[i])
    print('1111111######')
    idx = direction.index(D)
    # print('idx', idx)
    for i in range(N):
        for j in range(N):
            if NN[i][j] != 0:
                # print(i, j)
                for k in range(1, N-i):
                    # 이동 방향이므로 확인하는 좌표는 반대(-)로 확인
                    if NN[i+dy[idx]*(-k)][j+dx[idx]*(-k)] != 0:
                        # print('k', k, NN[i+dy[idx]*(-k)][j+dx[idx]*(-k)])
                        if NN[i+dy[idx]*(-k)][j+dx[idx]*(-k)] == NN[i][j]:
                            NN[i][j] = NN[i][j] * 2
                            NN[i + dy[idx] * (-k)][j + dx[idx] * (-k)] = 0
                            for h in NN:
                                print(h, end='\n')
                            print('########')
                        break

    for i in range(N):
        for j in range(N):
            if NN[i][j] != 0:
                if i == 1 and NN[i + dy[idx]][j + dx[idx]] == 0:
                    NN[i + dy[idx]][j + dx[idx]], NN[i][j] = NN[i][j], 0
                elif i > 1 and NN[i+dy[idx]][j+dx[idx]] == 0:
                    for k in range(1, i+1):
                        if NN[i+dy[idx]*(k+1)][j+dx[idx]*(k+1)] != 0 and NN[i+dy[idx]*k][j+dx[idx]*k] == 0:
                            NN[i+dy[idx]*k][j+dx[idx]*k], NN[i][j] = NN[i][j], 0
                            break
    print('#%d' % tc)
    for i in NN:
        print(i, end='\n')






