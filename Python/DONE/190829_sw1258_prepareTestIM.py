import sys
sys.stdin = open('sw1258.txt', 'r')
from collections import deque

# 다현언니 풀이 참고해서 수정
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    storage = [[0]*(N+2)] + [([0] + list(map(int, input().split())) + [0]) for _ in range(N)] + [[0]*(N+2)]
    boxes = deque('')

    for i in range(1, N+1):
        for j in range(1, N+1):
            if storage[i][j] and storage[i-1][j] + storage[i][j-1] == 0:
                for x in range(j+1, N+1):
                    if storage[i][x] == 0:
                        break
                width = x-j
                for y in range(i+1, N+1):
                    if storage[y][j] == 0:
                        break
                height = y-i
                boxes.append([width*height, height, width])
    boxes = list(boxes)
    boxes.sort()
    result = ''
    for i in boxes:
        result += ' ' + str(i[1]) + ' ' + str(i[2])
    print('#%d %d%s' % (tc, len(boxes), result))


# # 첫 번째 풀이
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     storage = [[0]*(N+2)] + [([0] + list(map(int, input().split())) + [0]) for _ in range(N)] + [[0]*(N+2)]
#
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if storage[i][j]:
#                 if storage[i-1][j] + storage[i][j-1] == 0:
#                     storage[i][j] = 1
#                 elif storage[i-1][j]:
#                     storage[i][j] = storage[i-1][j] + 1
#                 else:
#                     storage[i][j] = storage[i][j-1] + 1
#
#     for i in storage:
#         print(i, end='\n')
#     print('##########')
#
#     boxes = []
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if storage[i][j] and storage[i][j+1] + storage[i+1][j] == 0:
#                 a = i
#                 while storage[a][j]:
#                     a -= 1
#                 width = storage[a + 1][j]
#                 height = storage[i][j] - width + 1
#                 boxes.append([width*height, height, width])
#     boxes.sort()
#     # print(boxes)
#     result = ''
#     for i in boxes:
#         result += ' ' + str(i[1]) + ' ' + str(i[2])
#     print('#%d %d%s' % (tc, len(boxes), result))
