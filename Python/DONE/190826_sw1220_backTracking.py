import sys
sys.stdin = open('sw1220.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    table = [input().split() for _ in range(N)]

    # 자석 나오는지 확인(True/False) (인덱스로 구분하기 쉽게 0인덱스도 추가하고 count값을 저장)
    # 실질적으로 check[1]값은 필요가 없음(값을 저장할 필요가 없기 때문에)
    check = [0, 0, 0]
    for i in range(N):
        for j in range(N):
            if table[j][i] == '1':
                check[1] = 1
            elif table[j][i] == '2':
                if check[1]:
                    check[0] += 1
                    check[1] = 0
        if check[1]:
            check[1] = 0

    print('#%d %d' % (tc, check[0]))



# 첫 번째 풀이: 90도 회전해서 풀이
for tc in range(1, 11):
    N = int(input())
    table = [[0] * N for _ in range(N)]
    # 입력받은 input값을 90도 회전하여 입력
    # (위아래로 떨어지는 것이 아니라 양옆으로 움직여서 계산하기 쉽도록 형태변환)
    for i in range(N):
        input_row = input().split()
        for j in range(N):
            table[j][-1 - i] = input_row[j]

    # 자석 나오는지 확인(True/False) (인덱스로 구분하기 쉽게 0인덱스도 추가하고 count값을 저장)
    # 실질적으로 check[1]값은 필요가 없음(값을 저장할 필요가 없기 때문에)
    check = [0, 0, 0]
    for i in range(N):
        for j in range(N):
            if table[i][j] == '2':
                check[2] = 1
            elif table[i][j] == '1':
                if check[2]:
                    check[0] += 1
                    check[2] = 0
        if check[2]:
            check[2] = 0

    print('#%d %d' % (tc, check[0]))