def solution(s):
    answer = []
    numbers = s[2:-2].split('},{')
    for i in range(len(numbers)):
        numbers[i] = list(map(int, numbers[i].split(',')))
        numbers[i] = [len(numbers[i])] + numbers[i]
    numbers.sort()
    for i in numbers:
        for j in i[1:]:
            if j not in answer:
                answer.append(j)
    return answer