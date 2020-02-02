import sys
sys.stdin = open('sw4836_input.txt', 'r')

# 테스트 케이스 개수 T / 첫 줄에 칠할 영역의 개수 N
# 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color ( 0 ≤ r1, c1, r2, c2 ≤ 9 ) / color = 1 (빨강), color = 2 (파랑)
T = int(input())
for tc in range(T):
    N = int(input())
    squares = [0] * N
    squares_colors = [[] for _ in range(N)]
    for i in range(N):  # squares 상세정보 입력받기 (N개)
        squares[i] = list(map(int, input().split()))
        for r in range(squares[i][0], squares[i][2]+1):
            for c in range(squares[i][1], squares[i][3]+1):
                squares_colors[i].append((r, c))

    comparison = []  # square 조합할 수 있는 경우의 수 찾기
    for x in range(len(squares)):
        for y in range(x + 1, len(squares)):
            if squares[x][4] - squares[y][4]:
                comparison.append((x, y))
    result = []
    for c in comparison:
        for a in squares_colors[c[0]]:
            if a in squares_colors[c[1]]:
                result.append(a)

    print('#{} {}'.format(tc+1, len(set(result))))
