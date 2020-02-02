import sys
sys.stdin = open('bj2669.txt', 'r')

squares = [list(map(int, input().split())) for _ in range(4)]
# 사각형의 정보 입력 [[1, 2, 4, 4], [2, 3, 5, 7], [3, 1, 6, 5], [7, 3, 8, 6]]

maxN = 0  # 사각형이 있는 곳을 색칠할(1로 표시함) 도화지 만들기
for s in squares:
    for i in s:
        if i > maxN:
            maxN = i
graph = [[0] * maxN for _ in range(maxN)]

for s in squares:  # 각 사각형마다 도화지에 색칠 (중복되더라도 1로 유지되므로 중복처리할 수 있음)
    for i in range(s[0], s[2]):
        for j in range(s[1], s[3]):
            graph[i][j] = 1

result = 0
for n in graph:    # 도화지에 색칠된 곳을 합해서 출력
    # print(n, end='\n')
    result += sum(n)

print(result)