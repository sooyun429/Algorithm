import sys
sys.stdin = open('bj10163.txt', 'r')


# def prange(s, n):  # 색종이의 변의 길이 좌표 범위를 반환해주는 함수
#     return range(papers[s][n], papers[s][n] + papers[s][n+2])
#
# N = int(input())
# papers = [list(map(int, input().split())) for _ in range(N)]
#
# for p in range(len(papers)):
#     # 색종이를 놓는 (색칠할) 보드 만들기 (가로세로 최대 101칸)
#     # 매번 계산할 때마다 초기화해서 계산해야 하므로 반복문 안에 넣는다.
#     board = [[0] * 101 for _ in range(101)]
#     result = 0
#
#     for i in prange(p, 0):
#         for j in prange(p, 1):
#             board[i][j] = 1
#
#     # p보다 위에 있는 색종이들(up)을 체크해서 겹치는 부분에서 1을 0으로 바꾼다
#     for up in range(p+1, len(papers)):
#         for i in prange(up, 0):
#             for j in prange(up, 1):
#                 board[i][j] = 0
#
#     for i in range(101):
#         result += sum(board[i])
#     print(result)



## up 색종이를 처리하는 부분에서 범위 지정해서 처리(시간이 더 걸린다..?)


def prange(s, n):  # 색종이의 변의 길이 좌표 범위를 반환해주는 함수
    return range(papers[s][n], papers[s][n] + papers[s][n+2])

N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]

for p in range(len(papers)):
    # 색종이를 놓는 (색칠할) 보드 만들기 (가로세로 최대 101칸)
    # 매번 계산할 때마다 초기화해서 계산해야 하므로 반복문 안에 넣는다.
    board = [[0] * 101 for _ in range(101)]
    result = 0

    for i in prange(p, 0):
        for j in prange(p, 1):
            board[i][j] = 1

    # p보다 위에 있는 색종이들(up)을 체크해서 겹치는 부분에서 1을 0으로 바꾼다
    for up in range(p+1, len(papers)):
        if papers[up][0] > papers[p][0]+papers[p][2] or papers[up][0] + papers[up][2] < papers[p][0] or papers[up][1] > papers[p][1] + papers[p][3] or papers[up][1] + papers[up][3] < papers[p][1]:
            continue
        else:
            for i in prange(up, 0):
                for j in prange(up, 1):
                    board[i][j] = 0

    for i in range(101):
        result += sum(board[i])
    print(result)
