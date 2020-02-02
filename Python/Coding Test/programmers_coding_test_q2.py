def solution(n):
    if n == 1:
        return [0]
    else:
        before = solution(n-1)
        idx = len(before)//2
        half_a_half = before[:idx]
        half_a = half_a_half + [0] + 
        [(half_a_half[i]+1)%2 for i in range(len(half_a_half)-1, -1, -1)]
        half_b = [(half_a[i]+1)%2 for i in range(len(half_a)-1, -1, -1)]
        answer = half_a+[0]+half_b
        return answer