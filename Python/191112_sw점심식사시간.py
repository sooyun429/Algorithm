import sys
sys.stdin = open('sw점심식사시간.txt', 'r')

for tc in range(1, int(input())+1):
    N, NN, exits = int(input()), [], []
    # for i in NN: print(i)
    print('###########')
    for i in range(N): # NN 정보 입력하면서 입구정보 받아놓기
        NN.append(list(map(int, input().split())))
        for j in range(N):
            if NN[i][j] and NN[i][j] != 1:
                exits.append([i, j, NN[i][j], [0, 0, 0]]) # (좌표값과 계단 높이)

    # # 사람별로 가까운 입구에 input (2개 입구와의 거리 비교하여 결정)
    # people = [[], []]
    # for i in range(N):
    #     for j in range(N):
    #         if NN[i][j] == 1:
    #             # route1 = abs(i - exits[0][0]) + abs(j - exits[0][1]) + exits[0][2]
    #             # route2 = abs(i - exits[1][0]) + abs(j - exits[1][1]) + exits[1][2]
    #             # print(i, j, route1, route2)
    #             # if route1 > route2:
    #             #     exits[1][3].append(route2 - exits[1][2] + 1)
    #             # else:
    #             #     exits[0][3].append(route1 - exits[0][2] + 1)
    #             ## 다른 방법...
    #             exit1 = abs(i - exits[0][0]) + abs(j - exits[0][1]) + exits[0][2] + 1
    #             exit2 = abs(i - exits[1][0]) + abs(j - exits[1][1]) + exits[1][2] + 1
    #             if exit1 > exit2:
    #                 people[1].append([exit2 - exits[1][2], [exit1 - exits[0][2]], [exit1, exit2]])
    #             else:
    #                 people[0].append([exit1 - exits[0][2], [exit2 - exits[1][2]], [exit1, exit2]])
    # people[0].sort()
    # people[1].sort()
    # # escape = [[1 for _ in range(len(people[0]))], [1 for _ in range(len(people[1]))]]
    # # print(escape)
    # print(exits, '//exits')
    # print('//people\n', people)
    # switch = 0
    # exit_idx = [0, 0]
    # while exit_idx[0] < len(people[0]) or exit_idx[1] < len(people[1]):
    #     flag = 1
    #     if exits[switch][3][0] <= people[switch][exit_idx[switch]][0]:
    #         exits[switch][3][0] = people[switch][exit_idx[switch]][2][switch]
    #         exits[switch][3].sort()
    #         exit_idx[switch] += 1
    #         flag = 0
    #     else:
    #         print(exit_idx, exits, '//exits changed')
    #         if flag:
    #             a = exits[switch][3][0]+exits[switch][2]
    #             b = people[switch][exit_idx[switch]][2][(switch+1)%2] if exits[(switch)+1)%2][3][0] <= people[switch][exit_idx[switch]][1][0] else exits[(switch+1)%2][3][0]+exits[(switch+1)%2][2]
    #         else:
    #             switch = (switch + 1) % 2

    #### 다르게 생각해보자...
    # 사람별로 가까운 입구에 input (2개 입구와의 거리 비교하여 결정)
    people = []
    for i in range(N):
        for j in range(N):
            if NN[i][j] == 1:
                exit1 = abs(i - exits[0][0]) + abs(j - exits[0][1]) + 1
                exit2 = abs(i - exits[1][0]) + abs(j - exits[1][1]) + 1
                people.append([exit1, exit2])
    escape = [1 for _ in range(len(people))]
    time = 0
    while sum(escape):
        time += 1
        for i in range(len(people)):
            
    print(exits)
    print(people)
    # switch = 0
    # exit_idx = [0, 0]
    # while exit_idx[0] < len(people[0]) or exit_idx[1] < len(people[1]):
    #     flag = 1
    #     if exits[switch][3][0] <= people[switch][exit_idx[switch]][0]:
    #         exits[switch][3][0] = people[switch][exit_idx[switch]][2][switch]
    #         exits[switch][3].sort()
    #         exit_idx[switch] += 1
    #         flag = 0
    #     else:
    #         print(exit_idx, exits, '//exits changed')
    #         if flag:
    #             a = exits[switch][3][0]+exits[switch][2]
    #             b = people[switch][exit_idx[switch]][2][(switch+1)%2] if exits[(switch)+1)%2][3][0] <= people[switch][exit_idx[switch]][1][0] else exits[(switch+1)%2][3][0]+exits[(switch+1)%2][2]
    #         else:
    #             switch = (switch + 1) % 2
