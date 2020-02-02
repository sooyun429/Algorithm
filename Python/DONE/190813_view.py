import sys
sys.stdin = open('input.txt', 'r')

T = 10
for i in range(1, T + 1):
    n = int(input())
    buildings = list(map(int, input().split()))
    proper_floors = [0] * n
    for j in range(2, n- 2):
        comparison = buildings[j - 2: j + 3]
        comparison.remove(buildings[j])
        if max(comparison) < buildings[j]:
            proper_floors[j] = buildings[j] - max(comparison)
    result = sum(proper_floors)
    print('#%d %d' % (i, result))
