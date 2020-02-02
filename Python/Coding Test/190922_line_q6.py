n, a = map(str, input().split())
n = int(n)
data = [[0, 0] for _ in range(n)]
maxnum = 0
for i in range(n):
    A, B = map(str, input().split())
    data[i][0] = int(A)
    
    if data[i][0] > maxnum: # 배열의 높이(최대 n) 구하기
        maxnum = data[i][0]
        
    temp = list(B)  # 숫자값 리스트 인트값으로 넣기
    for j in range(len(temp)):
        temp[j] = int(temp[j])
    data[i][1] = temp
    # [[5, [1, 2, 3]], [3, [4, 5]], [5, [7, 8, 9, 0]], [3, [6]]]
    # w += data[i][0]  # 배열의 가로 길이 구하기
h = maxnum*2-1

for i in range(len(data)):
    w = data[i][0]
    if a == 'TOP': sidx = 0  # 정렬 방식에 따라 시작점 설정
    elif a == 'MIDDLE': sidx = maxnum-w
    else: sidx = (maxnum-w)*2
        
    for j in range(len(data[i][1])):
        mark = []
        blank = '.'*w
        for k in range(0, sidx):  # 시작지점 이전까지 '...'으로 채워넣기
            mark.append(blank)
        num = data[i][1][j]
        if num == 1:
            mark += ['.'*(w-1)+'#' for _ in range(w*2-1)]
        elif num in [0, 2, 3, 5, 7, 8, 9]:
            mark += ['#'*w]
            if num == 0:
                mark += [('#'+'.'*(w-2)+'#') for _ in range(2*w-3)]
                mark += ['#'*w]
            elif num == 7:
                mark += ['.'*(w-1)+'#' for _ in range(2*w-2)]
            else:
                if num in [8, 9]:
                    mark += [('#'+'.'*(w-2)+'#') for _ in range(w-2)]
                elif num in [2, 3]:
                    mark += ['.'*(w-1)+'#' for _ in range(w-2)]
                else:
                    mark += ['#' + '.'*(w-1) for _ in range(w-2)]
                mark += ['#'*w]
                if num == 9:
                    mark += ['.'*(w-1)+'#' for _ in range(w-1)]
                else:
                    if num == 2:
                        mark += ['#' + '.'*(w-1) for _ in range(w-2)]
                    elif num == 8:
                        mark += [('#'+'.'*(w-2)+'#') for _ in range(w-2)]
                    else:
                        mark += ['.'*(w-1)+'#' for _ in range(w-2)]
                    mark += ['#'*w]
        elif num == 4:
            mark += [('#'+'.'*(w-2)+'#') for _ in range(w-1)]
            mark += ['#'*w]
            mark += ['.'*(w-1)+'#' for _ in range(w-1)]
        else:
            mark += [('#'+'.'*(w-1)) for _ in range(w-1)]
            mark += ['#'*w]
            mark += [('#'+'.'*(w-2)+'#') for _ in range(w-2)]
            mark += ['#'*w]
        for k in range(h-len(mark)):  # 남은 구간까지 '...'으로 채워넣기
            mark.append(blank)
        data[i][1][j] = mark
    # [[5, [1, 2, 3]], [3, [4, 5]], [5, [7, 8, 9, 0]], [3, [6]]]
# print(data)
for i in range(h):
    temp = ''
    for j in range(len(data)):
        for k in range(len(data[j][1])):
            temp += data[j][1][k][i] + ' '
    print(temp[:-1])