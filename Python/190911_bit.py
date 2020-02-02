# 비트 연산

def Bbit_print(i):  # 좀 더 공부하기(이해하기)
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
        print(output)


for i in range(-5, 6):
    print('%3d = ' % i, end='')
    Bbit_print(i)


## 연습문제 1
a = '00000010001101'
b = '0000000111100000011000000111100110000110000111100111100111111001100111'


def decimal(n):
    result = [0]*(len(n)//7)
    for i in range(len(n)//7):
        cal = 0
        for j in range(7):
            cal += (2**(6-j))*int(n[7*i+j])
        result[i] = str(cal)
    return ', '.join(result)


print(decimal(a))
print(decimal(b))


# 비트연산 예제3
n = 0x00111111

if n & 0xff:
    print(n)
    print(n&0xff)
    print('little endian')
else:
    print(n)
    print('big endian')




## 비트연산 예제 5


def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
        print(output)


a = 0x86
key = 0xAA

print('a ==> ', end='')
Bbit_print(a)

print('a^=key ==> ', end='')
a ^= key
Bbit_print(a)

print('a^=key ==> ', end='')
a ^= key
Bbit_print(a)