def solution(n, lost, reserve):
    answer = [1]*(n+1)
    for i in lost:
        answer[i] -= 1
    for i in reserve:
        if answer[i]==0: # 도난당한 사람이라면 자기가 써야함
            answer[i] += 1
        else:
            if i > 1 and answer[i-1] == 0:
                answer[i-1] += 1
            elif i < n and answer[i+1] == 0:
                answer[i+1] += 1
    return sum(answer)-1