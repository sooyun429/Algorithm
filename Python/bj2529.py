import sys
sys.stdin = open('bj2529.txt', 'r')

import itertools
for x in range(3):
    N = int(input())
    array = list(map(str, input().split()))
    lists = list(itertools.permutations(range(0, 10), N+1))
    # print(lists)
    # print(array)

    for li in lists[::-1]:
        # temp = list(li)
        for idx in range(N):
            if array[idx] == '<':
                if li[idx] >= li[idx+1]:
                    break
            elif array[idx] == '>':
                if li[idx] <= li[idx+1]:
                    break
        else:
            res_max = ''
            for num in list(li):
                res_max += str(num)
            break

    for li in lists:
        # temp = list(li)
        for idx in range(N):
            if array[idx] == '<':
                if li[idx] >= li[idx+1]:
                    break
            elif array[idx] == '>':
                if li[idx] <= li[idx+1]:
                    break
        else:
            res_min = ''
            for num in list(li):
                res_min += str(num)
            break

    print(res_min)
    print(res_max)
