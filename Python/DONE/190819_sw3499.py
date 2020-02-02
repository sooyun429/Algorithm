import sys
sys.stdin = open('sw3499_input.txt', 'r')

T = int(input())
for tc in range(T):
    N = int(input())
    words = list(map(str, input().split()))
    section = N//2
    result = ''
    for i in range(section):
        result += words[i] + ' ' + words[-section+i] + ' '
    if N%2:
        result += words[section] + ' '
    print('#%d %s' % (tc+1, result[:-1]))