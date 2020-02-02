import sys
sys.stdin = open('sw7465.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    groups = [[]]
    nums = []
    for i in range(M):
        a, b = map(int, input().split())
        nums += [a, b]
        flaga = 1
        for j in range(len(groups)):
            if a in groups[j]: ## a가 기존 그룹에 있는지 확인
                flagb = 1
                for k in range(len(groups)):
                    if b in groups[k]:  # a가 있으면서 b가 기존 그룹에 있는지 확인
                        if j != k:  # a, b가 들어있는 그룹이 다르면 그룹 합치기(같으면 nothing)
                            groups[j] += groups[k]
                            groups[k] = []
                        flagb = 0  # b가 있었음을 체크
                        break
                if flagb:  # a는 있는데 b는 안들어가 있으면 a 그룹에 b 추가
                    groups[j].append(b)
                flaga = 0
                break
        if flaga:  # a가 기존 그룹에 없는 경우
            flagb = 1
            for j in range(len(groups)):
                if b in groups[j]:  # b는 기존 그룹에 있으면 b 그룹에 a 추가
                    groups[j].append(a)
                    flagb = 0
                    break
            if flagb:  # a, b 둘 다 기존 그룹에 없으면 새로 추가
                groups.append([a, b])
    result = 0
    for i in groups:
        if i:
            result += 1
    for i in range(1, N+1):
        if i not in nums:
            result += 1
    print('#%d %d' % (tc, result))
