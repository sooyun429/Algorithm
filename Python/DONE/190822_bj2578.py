import sys
sys.stdin = open('bj2578.txt', 'r')

board = [input().split() for _ in range(5)]  # 빙고판 만들기(2차원 배열) str 그대로 받아옴
numbers = input().split()  # 사회자가 부르는 숫자 1차원 배열로 만들기
for _ in range(4):
    numbers += input().split()

number = 0
cnt = 0
checkbox = [[0]*5] + [[0]*5] + [[0]] + [[0]]  # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 0, 0] 가로 세로 정방향대각선, 역방향대각선

while cnt < 3:  # 빙고인지 반복문으로 체크
    for i in range(5):  # 사회자가 부른 숫자가 일치하면 'X'로 변경
        for j in range(5):
            if board[i][j] == numbers[number]:
                board[i][j] = 'X'
                checkbox[0][i] += 1
                checkbox[1][j] += 1
                if i == j:
                    checkbox[2][0] += 1
                if i+j == 4:
                    checkbox[3][0] += 1
    number += 1

    cnt = 0  # 빙고의 개수 반복문 돌때마다 체크
    for i in checkbox:
        for j in i:
            if j == 5:
                # for n in range(5):
                #     print(board[n], end='\n')
                cnt += 1
print(number)