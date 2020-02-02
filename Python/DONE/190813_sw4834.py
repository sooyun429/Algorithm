import sys
sys.stdin = open('sw4834_input.txt', 'r')

T = int(input())
for i in range(T):
    N = int(input())
    cards = list(map(int, input()))
    countbox = {}
    for card in cards:
        if card not in countbox:
            countbox[card] = cards.count(card)
    same_values = []
    for k, v in countbox.items():
        if v == max(countbox.values()):
            same_values.append(k)
    same_values.sort()
    print('#%d %d %d' % (i + 1, same_values[-1], max(countbox.values())))
