import sys
sys.stdin = open('sw4865_input.txt', 'r')

T = int(input())
for tc in range(T):
    str1 = set(input())
    str2 = list(input())
    max_cnt = 0
    for i in str1:
        if max_cnt < str2.count(i):
            max_cnt = str2.count(i)
    print('#%d %d' % (tc+1, max_cnt))
