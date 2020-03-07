import itertools

def solution(weight):
    arr = []
    res_arr = [i for i in range(1, sum(weight))]
    for i in range(1, len(weight)):
        temp = list(itertools.combinations(weight, i))
        for j in range(len(res_arr)):
            if res_arr[j] in temp:
                res_arr = res_arr[:j]+res_arr[j+1:]
    answer = res_arr[0]
                    
    return answer