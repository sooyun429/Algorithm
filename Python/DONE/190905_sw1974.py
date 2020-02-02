import sys
sys.stdin = open('sw1974.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for i in range(9):
        if sum(sudoku[i]) != 45:  # 1-9까지 합계(45)가 아닌 경우 break
            result = 0
            break
        else:  # 합계가 같더라도 숫자는 다를 수 있으므로 추가 검사
            check = [0] + [1] * 9
            check2 = [0] + [1] * 9
            for j in range(9):
                check[sudoku[i][j]] = 0  # 가로 줄 검사
                check2[sudoku[j][i]] = 0  # 세로 줄 검사
            if sum(check) or sum(check2):
                result = 0
                break
    if result:  # 3*3 배열 검사
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                check3 = [0] + [1] * 9
                for k in range(3):
                    for h in range(3):
                        check3[sudoku[i+k][j+h]] = 0
                if sum(check3):
                    result = 0
                    break
    print('#%d %d' % (tc, result))



# 중간에 합계 체크 없애도 실행시간은 비슷함
# T = int(input())
# for tc in range(1, T+1):
#     sudoku = [list(map(int, input().split())) for _ in range(9)]
#     result = 1
#     for i in range(9):
#         check = [0] + [1] * 9
#         check2 = [0] + [1] * 9
#         for j in range(9):
#             check[sudoku[i][j]] = 0  # 가로 줄 검사
#             check2[sudoku[j][i]] = 0  # 세로 줄 검사
#         if sum(check) or sum(check2):
#             result = 0
#             break
#     if result:  # 3*3 배열 검사
#         for i in range(0, 9, 3):
#             for j in range(0, 9, 3):
#                 check3 = [0] + [1] * 9
#                 for k in range(3):
#                     for h in range(3):
#                         check3[sudoku[i+k][j+h]] = 0
#                 if sum(check3):
#                     result = 0
#                     break
#     print('#%d %d' % (tc, result))
