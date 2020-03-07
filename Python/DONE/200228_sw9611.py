import sys  # 자바 또는 C++로 풀어봐야하는 문제
sys.stdin = open('sw9611.txt', 'r')

for tc in range(1, int(input())+1):
    candidates = [1 for _ in range(10)]
    N = int(input())
    for turn in range(N):
        numbers = input().split()
        if numbers[-1] == 'NO':
            for n in range(4):
                candidates[int(numbers[n])] = 0
        else:
            for n in range(4):
                candidates[int(numbers[n])] != 0
                candidates[int(numbers[n])] = 2

    for i in range(10):
        if candidates[i] == 2:
            print('#%d %d' % (tc, i))
            break
        elif sum(candidates) == 1 & candidates[i] == 1:
            print('#%d %d' % (tc, i))
            break
