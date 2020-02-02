import sys
sys.stdin = open('sw4522.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    word = list(input())
    reverse_word = word[::-1]
    result = 'Exist'
    for i in range(len(word)//2+1):
        if word[i] != reverse_word[i]:
            if word[i] == '?' or reverse_word[i] == '?':
                continue
            else:
                result = 'Not exist'
    print('#%d %s' % (tc, result))
