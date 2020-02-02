## 190819 strings_연습문제 1
s = 'Reverse this strings'
print(s[::-1])

strings = list(s)
result = ''
for s in range(len(strings)):
    result += strings[-1-s]
print(result)


## itoa 연습문제 2

int_num = 9  # 1001로 저장됨
string_num = ord('0') + int_num  # 111001로 저장됨
print(string_num)

print(123**(1/10))  # 1.618...
n = 123
string_n = []
for i in range(int(n**(1/10)+1), -1, -1):
    number = n//(10**i) - n//(10**(i+1))*10
    string_n.append(ord('0') + number)
print(string_n)


## 고지식한 방법 알고리즘 연습문제 3

sentence = 'a pattern matching algorithm'
words = 'rithm'
N = len(sentence)
M = len(words)
i = j = 0

while i < N and j < M:
    if sentence[i] != words[j]:
        i -= j
        j = -1
    i += 1
    j += 1
if j == M: print('일치')
else: print('불일치')
