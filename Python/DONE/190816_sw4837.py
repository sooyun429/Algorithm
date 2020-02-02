import sys
sys.stdin = open('sw4837_input.txt', 'r')

T = int(input())
arr = list(range(1, 13))

for tc in range(T):
    N, K = map(int, input().split())
    result = []
    for i in range(1, 1 << len(arr)):
        subset = []
        for j in range(len(arr)):
            if i & (1 << j):
                subset.append(arr[j])
        if len(subset) == N and sum(subset) == K:
            result.append(subset)
    print('#%d %d' % (tc+1, len(result)))

