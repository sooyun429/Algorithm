import sys, itertools
sys.stdin = open('q2.txt', 'r')

import itertools

T = int(input())
perm = list(itertools.permutations(list(range(6))))
for _ in range(T):
    tc = int(input())
    NN = [input().split() for _ in range(10)]
    # robot과 snack의 좌표값을 저장하여 사용
    robot = [0]*6
    snack = [0]*6
    ridx = sidx = 0
    for i in range(10):
        for j in range(10):
            num = NN[i][j]
            if num != '0':
                if num == '9':
                    robot[ridx] = [i, j]
                    ridx += 1
                else:
                    snack[sidx] = [i, j]
                    sidx += 1
            if ridx == 6 and sidx == 6:
                break
    result = 200
    for i in perm:  # 저장해 둔 순열조합(list(range(6)) 경우의 수에 따라 거리 계산
        temp = 0
        for j in range(6):
            temp += abs(robot[j][0]-snack[i[j]][0]) + abs(robot[j][1]-snack[i[j]][1])
            if temp >= result:
                break
        if temp < result:
            result = temp
    print('#%d %d' % (tc, result))
