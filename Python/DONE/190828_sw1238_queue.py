import sys
sys.stdin = open('sw1238.txt', 'r')

for tc in range(1, 11):
    n, s = map(int, input().split())
    numbers = list(map(int, input().split()))
    edges = [[0] * 101 for _ in range(101)]
    # 간선정보 (중복값은 덮어지면서 제거됨)
    check_imax = 0
    for i in range(0, len(numbers), 2):
        edges[numbers[i]][numbers[i+1]] = numbers[i+1]
        # 나가는 선이 있는 vortex 최대값 구해서 나중에 edges 필요없는 항목 제거할 때 사용
        if numbers[i] > check_imax:
            check_imax = numbers[i]
    edges = edges[:check_imax+1]
    # 각 vortex별로 갈 수 있는 번호 정보 통해 연락 작업 진행
    level = [[] for _ in range(50)]
    level[0] = [s]
    level_cnt = 0
    visited = [0] * 101
    visited[s] = 1

    while True:
        level_cnt += 1
        for i in level[level_cnt-1]:
            # visited[i] = 1  # 여기서 visited 체크해주면 에러가 남
            if i < len(edges):
                for j in edges[i]:
                    if j and visited[j] == 0 and (j not in level[level_cnt]):
                        level[level_cnt].append(j)
                        visited[j] = 1  # 그래서 j를 넣고나자마자 visited 체크해야 함
        if len(level[level_cnt]) == 0:
            break

    level[level_cnt-1].sort()
    print('#%d %d' % (tc, level[level_cnt-1][-1]))
