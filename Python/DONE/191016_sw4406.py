import sys
sys.stdin = open('sw4406.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    result = ''
    vowels = 'aeiou'
    word = input()
    for letter in word:
        if letter not in vowels:
            result += letter
    print('#%d %s' % (tc, result))
