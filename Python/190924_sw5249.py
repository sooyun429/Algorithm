import sys
sys.stdin = open('sw5249.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    N = V+1  # 총 정점의 갯수
    NN = [0]*(N**2)  # 1차원 배열로 가중치를 입력(인덱스 계산으로 찾을 예정)
    for i in range(E):
        a, b, w = map(int, input().split())
        NN[a*N + b] = w  # 무방향이지만 굳이 두 번 저장할 필요 없음

    visited = [0]*N  # 방문한 정점 체크
    result = 0
    while sum(visited) != N:  # 전체 가중치 중 min값 찾기
        temp = 20
        for i in NN:
            if i and (temp > i):
                temp = i
        result += temp
        # min값으로 인덱스 찾아 x,y좌표 찾기
        # 중복인 경우 제일 앞에 있는 좌표를 가져옴
        minidx = NN.index(temp)
        minx = minidx // N
        miny = minidx % N
        visited[minx] = visited[miny] = 1  # 방문표시 해주고

        # while문 돌 때마다 양 정점 a, b 모두 방문한 곳 간선은 필요없으므로 0으로 바꿔줌
        for i in range(N):
            for j in range(i+1, N):
                if visited[i] == 1 and visited[j] == 1:
                    NN[i*N+j] = NN[j*N+i] = 0

    print('#%d %d' % (tc, result))


# ## 최소신장트리의 조건을 만족하지 못함(3개만 맞음)
# ## 모든 노드가 하나의 줄로 연결되어 있어야 함 (1개의 그룹)
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     N = V+1  # 총 정점의 갯수
#     NN = [0]*(N**2)  # 1차원 배열로 가중치를 입력(인덱스 계산으로 찾을 예정)
#     for i in range(E):
#         a, b, w = map(int, input().split())
#         NN[a*N + b] = w  # 무방향이지만 굳이 두 번 저장할 필요 없음
#     visited = [0]*N  # 방문한 정점 체크
#     result = 0
#
#     while sum(visited) != N:  # 전체 가중치 중 min값 찾기
#         temp = 20
#         for i in NN:
#             if i and (temp > i):
#                 temp = i
#         result += temp
#         print(NN, temp, result)
#         # min값으로 인덱스 찾아 x,y좌표 찾기
#         # 중복인 경우 제일 앞에 있는 좌표를 가져옴
#         minidx = NN.index(temp)
#         minx = minidx // N
#         miny = minidx % N
#         visited[minx] = visited[miny] = 1  # 방문표시 해주고
#
#         # while문 돌 때마다 양 정점 a, b 모두 방문한 곳 간선은 필요없으므로 0으로 바꿔줌
#         for i in range(N):
#             for j in range(i+1, N):
#                 if visited[i] == 1 and visited[j] == 1:
#                     NN[i*N+j] = NN[j*N+i] = 0
#
#     print('#%d %d' % (tc, result))
