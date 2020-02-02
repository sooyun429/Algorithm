import sys
sys.stdin = open('q1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    NN = [list(map(int, input().split())) for _ in range(N)]
    result = [[0]*N for _ in range(N)]
    result = 0
    minnum = 200
    for i in range(N):
        for j in range(N):
            hori = NN[i] # 가로 다리의 숫자들
            verti = [NN[k][j] for k in range(N)]  # 세로 다리의 숫자들

            a, b = min(NN[i]), max(NN[i])  # 살펴봐야 하는 높이의 범위 설정
            if min(verti) < a:
                a = min(verti)
            if max(verti) > b:
                b = max(verti)

            # i행과 j열 선택했을 때 최소 건설비용 나오는 높이 찾기
            # 최소값이 동일할 때 높이가 낮은 것으로 업데이트해야하므로 높이의 범위는 큰 값에서 작은값으로 감소
            for k in range(b, a-1, -1):
                temp = 0  # 건설에 소요되는 비용 저장
                for num in hori:
                    temp += abs(num-k)
                for num in verti:
                    temp += abs(num-k)
                temp -= abs(NN[i][j]-k)  # NN[i][j]는 두 번 계산되므로 뒤에서 한 번 빼주기
                if temp <= minnum:
                    result = k
                    minnum = temp
    print('#%d %d %d' % (tc, minnum, result))
