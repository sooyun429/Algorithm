import sys, time, itertools
sys.stdin = open('q3.txt', 'r')

# import itertools

T = int(input())
for tc in range(1, T+1):
    stime = time.time()
    N, M, C = map(int, input().split())
    NM = [list(map(int, input().split())) for _ in range(N)]
    # 로봇의 좌표값 저장
    robot = 0
    for i in range(N):
        for j in range(M):
            if NM[i][j] == 1:
                robot = [i, j]
                NM[i][j] = 0
                break
        if robot:
            break

    # 미네랄 정보(가는 데 필요한 에너지, 미네랄의 양) 저장
    minerals = [0]*20
    midx = 0
    for i in range(N):
        for j in range(M):
            if NM[i][j]:
                distance = (abs(robot[0]-i)+abs(robot[1]-j))*2
                if distance <= C:  # 애초에 갈 수 있는 미네랄 정보만 저장
                    minerals[midx] = [distance, NM[i][j]]
                    midx += 1
    minerals = minerals[:midx]
    result = 0

    for i in range(1, len(minerals)+1):
        com = list(itertools.combinations(list(range(len(minerals))), i))
        for j in com:
            move = save = 0
            for k in range(len(j)):
                move += minerals[j[k]][0]
                if move > C:
                    break
                save += minerals[j[k]][1]
            if save > result:
                result = save
    print('#%d %d %s' % (tc, result, time.time()-stime))
