import sys
sys.stdin = open('sw3282_input.txt', 'r')

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    # 입력받은 물건을 튜플(V, C) 형태로 리스트 안에 입력
    stuffs = [list(map(int, input().split())) for _ in range(N)]
    max_C = 0

    # 가방의 부피 K 만큼 담을 수 있는 경우의 수를 모두 추출(시프트 정렬 활용)
    for i in range(1, 1 << len(stuffs)):
        subset = []
        v = 0
        c = 0
        for j in range(len(stuffs)):
            if i & (1 << j):
                subset.append(stuffs[j])
                v += stuffs[j][0]
                c += stuffs[j][1]
        if v <= K and c > max_C:
            max_C = c

    print('#%d %d' % (tc+1, max_C))
