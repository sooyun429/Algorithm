import sys
sys.stdin = open('sw4676.txt', 'r')

for tc in range(1, int(input())+1):
    words = ['']+list(input())
    L = len(words)
    H = int(input())
    hyphen = list(map(int, input().split()))
    for h in hyphen:
        words[h] += '-'
    print('#%d %s' % (tc, ''.join(words)))