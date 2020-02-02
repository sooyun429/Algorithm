import sys
sys.stdin = open('bj2589.txt', 'r')


def around(a, b):  # 갈 수 있는 땅의 갯수를 체크
    venue = []
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    for i in range(4):
        if M[a+dy[i]][b+dx[i]] == 'L':
            venue.append([a+dy[i], b+dx[i]])
    return venue

r, c = map(int, input().split())
M = [['W']*(c+2)] + [(['W'] + list(input()) + ['W']) for _ in range(r)] + [['W']*(c+2)]
# print(M)
# for i in M:
#     print(i, end='\n')
result = 0
stack = []
for i in range(1, r+1):
    for j in range(1, c+1):
        path = around(i, j)
        if len(path) == 1:  ## 시작점이 튀어나오지 않은 경우도 있지 않을까? ex) 사각형 모양의 섬인 경우
            M[i][j] = 1
            cnt = 1
            while path:
                stack.append(path)  # 갈 수 있는 경로 1단계 저장

            # for k in path:


