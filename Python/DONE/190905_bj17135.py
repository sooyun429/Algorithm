import sys
sys.stdin = open('bj17135.txt', 'r')

## 첫 번째 시도 실패 (테스트 케이스만 맞음)
# def kill(row, col):
#     global land
#     for a in range(row - 1, row - D - 1, -1):  # 확인할 거리 최대 D만큼
#         if a < 0:
#             return
#         else:
#             for b in range(M):
#                 if land[a][b] and (abs(row-a) + abs(col-b)) <= D:
#                     land[a][b] = 0
#                     return 1
#
#
# for tc in range(6):
#     N, M, D = map(int, input().split())
#     original_land = [list(map(int, input().split())) for _ in range(N)]  # 적의 배치도 원본
#     # for i in original_land:
#     #     print(i, end='\n')
#     # print('#####')
#     max_result = 0
#     land = [[0] * M for _ in range(N)]
#     # 궁수 3명의 위치를 경우의 수별로 조합하여 최대 kill 수를 도출
#     for i in range(M):
#         for j in range(i+1, M):
#             for k in range(j+1, M):
#                 arrow = [i, j, k]
#                 result = 0
#                 for a in range(N):  # 매번 결과를 다시 봐야 하므로 행렬을 deepcopy하여 사용
#                     for b in range(M):
#                         land[a][b] = original_land[a][b]
#                 for row in range(N, 0, -1):  # 궁수 위치를 위로 올려간다 가정하고 계산
#                     for ar in arrow:
#                         k = kill(row, ar)
#                         if k:
#                             result += k
#                 if result > max_result:
#                     max_result = result
#     print(max_result)
#


## 두 번째 시도

# def kill(row, col):  # 최단거리에 죽일 수 있는 적이 있는지 체크하여 좌표값 반환
#     global land, D
#     for a in range(1, D+1):  # 확인할 거리 최대 D만큼
#         for b in range(1, a+1):  # i 좌표값 변화주는 변수
#             c = a - b
#             if row - b >= 0 and col - c >= 0 and land[row-b][col-c]:
#                 return [row-b, col-c, 1]
#             elif row-b >= 0 and col + c < M and land[row-b][col+c]:
#                 return [row - b, col + c, 2]
#             # if arrow == [0, 1, 3]:
#             #     for i in land:
#             #         print(i, end='\n')
#             #     print('######', cnt, ar, row, '#', a, b, c)
#
# for tc in range(7):
#     N, M, D = map(int, input().split())
#     original_land = [list(map(int, input().split())) for _ in range(N)]  # 적의 배치도 원본
#     max_result = 0
#     land = [[0] * M for _ in range(N)]
#     for i in range(M):  # 궁수 3명의 위치를 경우의 수별로 조합하여 최대 kill 수를 도출
#         for j in range(i+1, M):
#             for k in range(j+1, M):
#                 arrow = [i, j, k]
#                 result = 0
#                 for a in range(N):  # 매번 결과를 다시 봐야 하므로 행렬을 deepcopy하여 사용
#                     for b in range(M):
#                         land[a][b] = original_land[a][b]
#                 for row in range(N, 0, -1):  # 궁수 위치를 위로 올려간다 가정하고 계산
#                     cnt = [0] * 3
#                     temp = 0
#                     for ar in arrow:
#                         cnt[arrow.index(ar)] = kill(row, ar)
#                     # print('*****', arrow, row, cnt)
#                     for c in cnt:
#                         if c and land[c[0]][c[1]] == 1:
#                             land[c[0]][c[1]] = 0
#                             temp += 1
#                     result += temp
#                     # print(arrow, result, ar, row)
#                     # for i in land:
#                     #     print(i, end='\n')
#                     # print('#####')
#                 if result > max_result:
#                     max_result = result
#     print(max_result)


# 세 번째 시도
#
# def kill(row, col):  # 최단거리에 죽일 수 있는 적이 있는지 체크하여 좌표값 반환
#     global land, D
#     for a in range(1, D+1):  # 확인할 거리 최대 D만큼
#         for b in range(1, a+1):  # i 좌표값 변화주는 변수
#             c = a - b
#             if row - b >= 0 and col - c >= 0 and land[row-b][col-c]:
#                 return [row-b, col-c, 1]
#         for b in range(a, 0, -1):
#             c = a-b
#             if row-b >= 0 and col + c < M and land[row-b][col+c]:
#                 return [row - b, col + c, 2]
#             if arrow == [0, 2, 4]:
#                 for i in land:
#                     print(i, end='\n')
#                 print('######', cnt, ar, row, '#', a, b, c)
#
# for tc in range(1):
#     N, M, D = map(int, input().split())
#     original_land = [list(map(int, input().split())) for _ in range(N)]  # 적의 배치도 원본
#     max_result = 0
#     land = [[0] * M for _ in range(N)]
#     for i in range(M):  # 궁수 3명의 위치를 경우의 수별로 조합하여 최대 kill 수를 도출
#         for j in range(i+1, M):
#             for k in range(j+1, M):
#                 arrow = [i, j, k]
#                 result = 0
#                 for a in range(N):  # 매번 결과를 다시 봐야 하므로 행렬을 deepcopy하여 사용
#                     for b in range(M):
#                         land[a][b] = original_land[a][b]
#                 for row in range(N, 0, -1):  # 궁수 위치를 위로 올려간다 가정하고 계산
#                     cnt = [0] * 3
#                     temp = 0
#                     for ar in arrow:
#                         cnt[arrow.index(ar)] = kill(row, ar)
#                     print('*****', arrow, row, cnt)
#                     for c in cnt:
#                         if c and land[c[0]][c[1]] == 1:
#                             land[c[0]][c[1]] = 0
#                             temp += 1
#                     result += temp
#                 print(result)
#                 if result > max_result:
#                     max_result = result
#     print(max_result)


# 제출용 수정

def kill(row, col):  # 최단거리에 죽일 수 있는 적이 있는지 체크하여 좌표값 반환
    global land, D
    for a in range(1, D+1):  # 확인할 거리 최대 D만큼
        for b in range(1, a+1):  # i 좌표값 변화주는 변수
            c = a - b
            if row - b >= 0 and col - c >= 0 and land[row-b][col-c]:
                return [row-b, col-c, 1]
        for b in range(a, 0, -1):
            c = a-b
            if row-b >= 0 and col + c < M and land[row-b][col+c]:
                return [row - b, col + c, 2]

N, M, D = map(int, input().split())
original_land = [list(map(int, input().split())) for _ in range(N)]  # 적의 배치도 원본
max_result = 0
land = [[0] * M for _ in range(N)]
for i in range(M):  # 궁수 3명의 위치를 경우의 수별로 조합하여 최대 kill 수를 도출
    for j in range(i+1, M):
        for k in range(j+1, M):
            arrow = [i, j, k]
            result = 0
            for a in range(N):  # 매번 결과를 다시 봐야 하므로 행렬을 deepcopy하여 사용
                for b in range(M):
                    land[a][b] = original_land[a][b]
            for row in range(N, 0, -1):  # 궁수 위치를 위로 올려간다 가정하고 계산
                cnt = [0] * 3
                temp = 0
                for ar in arrow:
                    cnt[arrow.index(ar)] = kill(row, ar)
                for c in cnt:
                    if c and land[c[0]][c[1]] == 1:
                        land[c[0]][c[1]] = 0
                        temp += 1
                result += temp
            if result > max_result:
                max_result = result
print(max_result)
