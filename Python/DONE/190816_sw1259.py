import sys
sys.stdin = open('sw1259_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))  # [3, 4, 2, 3, 4, 5]
    pairs = [0] * n
    orders = []
    # 짝 지어주기 [[3, 4], [2, 3], [4, 5]]
    for i in range(n):
        pairs[i] = [numbers[2*i], numbers[2*i + 1]]

    orders.append(pairs[0])
    pairs.remove(pairs[0])
    while pairs:
        for pair in pairs:
            if pair[1] == orders[0][0]:
                orders.insert(0, pair)
                pairs.remove(pair)
            elif orders[-1][1] == pair[0]:
                orders.append(pair)
                pairs.remove(pair)

    result = ''
    for o in orders:
        for x in o:
            result += ' ' + str(x)

    print('#{}{}'.format(tc, result))