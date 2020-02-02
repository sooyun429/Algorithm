import sys
sys.stdin = open('sw4864_input.txt', 'r')

T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    s = str1[0]
    result = 0
    for l in range(len(str2)):
        if str2[l] == s:
            if str2[l:l + len(str1)] == str1:
                result = 1
                break
    print('#%d %d' % (tc + 1, result))
