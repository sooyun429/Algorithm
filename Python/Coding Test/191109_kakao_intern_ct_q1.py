def solution(board, moves):
    N = len(board)
    top = []
    answer = 0
    for i in moves:
        for j in range(N):
            present = board[j][i-1]
            if present:
                if len(top)==0 or present != top[-1]:
                    top.append(present)
                else:
                    answer += 2
                    top.pop(-1)
                board[j][i-1] = 0
                break
    return answer