import sys
sys.stdin = open('sw4047.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    s = input()
    YJ = [0] * (len(s)//3)
    result = ''

    # 입력받은 값에서 3개 단위로 끊어 리스트 생성 (영준이가 가지고 있는 카드)
    for i in range(0, len(s), 3):
        YJ[i//3] = s[i:i+3]

    YJ.sort()  # 검색 및 처리를 쉽게 하기 위해 카드덱 소트정렬
    cards = [['S', 13], ['D', 13], ['H', 13], ['C', 13]]

    for i in range(len(YJ)):  # 겹치는 카드가 있는지 확인 (정렬된 상태이므로 간단히 비교 가능함)
        if i != len(YJ)-1:
            if YJ[i] == YJ[i+1]:
                result = ' ERROR'
        for alphabet in cards:
            if alphabet[0] in YJ[i]:
                alphabet[1] -= 1

    if result != ' ERROR':
        for c in cards:
            result += ' ' + str(c[1])
    print('#%d%s' % (tc, result))
