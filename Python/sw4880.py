import sys
sys.stdin = open('sw4880.txt', 'r')

def tournament(s, e, a):
    if len(a) = 2:
        if a[0][1] > a[1][1]



    p = (s + e)//2 + 1


    box1 = a[:p]
    box2 = a[p:]


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 멤버의 번호와 카드 정보(번호 1, 2, 3)를 매칭
    nn = list(map(int, input().split()))
    print(nn)
    card = [[0, 0] for _ in range(N)]
    start, end = 0, N-1
    for i in range(N):
        card[i] = [i+1, nn[i]]
    print(card)

    # while card


# 1 3 3 3 1 1 3

a = [1, 2, 3, 4, 5]
b = a[:3]
print(b)