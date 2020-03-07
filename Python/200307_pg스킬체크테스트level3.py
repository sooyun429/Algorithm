def solution(n, computers):
    answer = []
    for i in range(n):
        if sum(computers[i]) == 1:
            answer += [[i]]
        else:
            for j in range(i+1, n):
                if computers[i][j]:
                    for k in range(len(answer)):
                        if i in answer[k]:
                            answer[k] += [j]
                            break
                    else:
                        answer += [[i, j]]
    return len(answer)