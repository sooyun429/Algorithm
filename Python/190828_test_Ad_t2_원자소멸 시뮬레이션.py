import sys
sys.stdin = open('190828_test_Ad_t2_원자소멸 시뮬레이션.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dots = [list(map(int, input().split())) for _ in range(N)]
    collision = [0] * (N*(N-1)//2)  # 충돌 정보 기록할 박스
    colidx = 0
    d = [0, 1, 2, 3]
    ## 이동 방향은 상(0), 하(1), 좌(2), 우(3)
    for i in range(len(dots)):
        for j in range(i+1, len(dots)):
            if dots[i][2] != dots[j][2]:  # 같은 방향의 원자들은 제외(가지치기)
                if dots[i][0] == dots[j][0]:  # 같은 직선(x축)상에 있는 경우
                    # 이동방향이 상하로 반대면서 충돌할 가능성이 있는지 체크
                    if (dots[i][2] == 0 and dots[j][2] == 1 and dots[i][1] < dots[j][1]) or (dots[i][2] == 1 and dots[j][2] == 0 and dots[j][1] < dots[i][1]):
                        collision[colidx] = str(abs(dots[i][1]-dots[j][1])//2) + ' ' + str(i) + ' ' + str(j)
                        colidx += 1
                elif dots[i][1] == dots[j][1]:  # 같은 직선(y축)상에 있는 경우
                    if (dots[i][2] == 2 and dots[j][2] == 3 and dots[j][0] < dots[i][0]) or (dots[i][2] == 3 and dots[j][2] == 2 and dots[i][0] < dots[j][0]):
                        collision[colidx] = str(abs(dots[i][0]-dots[j][0])//2) + ' ' + str(i) + ' ' + str(j)
                        colidx += 1
                # 수직관계일 때
                elif (dots[i][2] in d[:2] and dots[j][2] in d[2:]) or (dots[i][2] in d[2:] and dots[j][2] in d[:2]):
                    # 교점과의 거리가 같은지 체크
                    second = abs(dots[i][0]-dots[j][0])
                    if second == abs(dots[i][1]-dots[j][1]):
                        if dots[i][2] == 0 and dots[i][1] < dots[j][1]:
                            if (dots[j][2] == 2 and dots[i][0] < dots[j][0]) or (dots[j][2] == 3 and dots[i][0] > dots[j][0]):
                                collision[colidx] = str(second) + ' ' + str(i) + ' ' + str(j)
                                colidx += 1
                        elif dots[i][2] == 1 and dots[i][1] > dots[j][1]:
                            if (dots[j][2] == 2 and dots[i][0] < dots[j][0]) or (
                                    dots[j][2] == 3 and dots[i][0] > dots[j][0]):
                                collision[colidx] = str(second) + ' ' + str(i) + ' ' + str(j)
                                colidx += 1
                        elif dots[i][2] == 2 and dots[i][0]:
                        else:



                elif :



