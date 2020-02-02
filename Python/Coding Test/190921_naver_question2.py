def solution(drum):
    answer = 0
    N = len(drum)
    drum = [[0]*(N+2)] + drum + [[0]*(N+2)]
    for i in range(1, N):
        drum[i] = [0] + list(drum[i]) + [0]
    print(drum)
    mark = ['#', '*', '>', '<']
    dx = [1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for x in range(1, N+1):
        i, j = x, 1
        check = 0
        flag = 0
        while i < N+1:
            D = drum[i][j] 
            if D:
                if check == 0:
                    if D == '*':
                        check = 1
                    i += dx[mark.index(D)]
                    j += dy[mark.index(D)]
                else:
                    if drum[i][j] == '*' and i <= N:
                        flag = 1
                        break
                    i += dx[mark.index(drum[i][j])]
                    j += dy[mark.index(drum[i][j])]
            else: break
        if not flag:
            answer += 1
    return answer