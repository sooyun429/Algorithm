import itertools

numbers = ['124783', '667767', '054060', '101123']

def combination(s):
    result = []
    if len(s) == 1:
        return s
    elif len(s) == 2:
        return [s[1], s[0]]
    else:
        for i in range(len(s)):
            s = [s[i]] + s[:i] + s[i+1:]
            s = [s[0]] + combination(s[1:])
        result.append(s)
        print(result)
        return result


for i in numbers:
    tempset = [0]*len(i)
    for j in range(len(i)):
        tempset[j] = int(i[j])
    # print(tempset)
    # print(combination(tempset))
    # combination = itertools.permutations(tempset)
    result = ':('
    for j in combination:
        cnt = 0
        if j[1]*2 == j[0]+j[2] and (abs(j[0]-j[2]) == 2 or j[0] == j[2]):
            cnt += 1
        if j[4]*2 == j[3]+j[5] and (abs(j[3]-j[5]) == 2 or j[3] == j[5]):
            cnt += 1
        if cnt == 2:
            result = 'baby-gin!'
            break
    print(i, result)