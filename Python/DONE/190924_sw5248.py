import sys
sys.stdin = open('sw5248.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    inputdata = list(map(int, input().split()))
    groups = [inputdata[:2]]
    for i in range(1, M):
        a, b = inputdata[i*2], inputdata[i*2+1]
        flaga = flagb = 101
        for j in range(len(groups)): # a, b가 기존 그룹에 있으면 인덱스 저장
            if a in groups[j]: flaga = j
            if b in groups[j]: flagb = j
        if flaga == 101 and flagb == 101: # a, b 둘 다 새로 입력하는 경우
            groups.append([a, b])
        elif flaga != 101 and flagb == 101: # b만 새로 입력하는 경우 a 그룹에 b 추가
            groups[flaga].append(b)
        elif flaga == 101 and flagb != 101: # a만 새로 입력하는 경우 b 그룹에 a 추가
            groups[flagb].append(a)
        else: # 둘 다 기존 그룹에 있는 경우
            if flaga != flagb: # a,b 들어있는 그룹이 다르면 두 그룹 합치기
                groups[flaga] += groups[flagb]
                groups[flagb] = [] # 합치고 나면 b그룹은 공집합처리
    cnt = 0
    for i in range(1, N+1): # 누구에게도 선택받지 못한 번호 count
        flag = 1
        for j in groups:
            if i in j:
                flag = 0
                break
        if flag:
            cnt += 1
    for i in groups: # 그룹 개수 카운트 ([] 비어있는 그룹도 있으므로)
        if i:
            cnt += 1
    print('#%d %d' % (tc, cnt))
