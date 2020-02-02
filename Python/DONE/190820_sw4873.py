import sys
sys.stdin = open('sw4873_input.txt', 'r')

T = int(input())
for tc in range(T):
    s = list(input())  # ['A', 'B', 'C', 'C', 'B']
    flag = True
    while flag:
        if len(s) == 1:
            flag = False
        for i in range(len(s)-1):
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2:]
                break
            if len(s) == 1:
                flag = False
                break
            if i == len(s) - 2:
                flag = False
                break
    print('#%d %d' % (tc + 1, len(s)))
