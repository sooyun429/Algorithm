## 진수 연습문제 2

def binary(n):
    global sixteen
    def decimal(m):
        result = [0] * (len(m) // 7)
        for i in range(len(m) // 7):
            tempnum = 0
            for j in range(7):
                tempnum += (2 ** (6 - j)) * int(m[i * 7 + j])
            result[i] = str(tempnum)

        if len(m)%7:
            lastpart = m[-(len(m)%7):]
            tempnum = 0
            for i in range(len(lastpart)):
                tempnum += (2 ** (len(lastpart)-1-i)) * int(lastpart[i])
            result.append(str(tempnum))
        return ', '.join(result)


    save =''
    for i in n:
        templist = [0, 0, 0, 0]
        v = sixteen.index(i)
        cnt = 3
        while cnt >= 0:
            templist[cnt] = str(v % 2)
            cnt -= 1
            v //= 2
        save += ''.join(templist)
    return decimal(save)


sixteen = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
a = '0F97A3'
b = '01D06079861D79F99F'
print(binary(a))
print(binary(b))




## 연습문제3


def binary(n):
    def findpattern(m):
        pattern = []
        idx = len(m) - 1
        while idx > 4:
            if m[idx] == '1' and (m[idx - 5:idx + 1] in password):
                pattern.insert(0, str(password.index(m[idx - 5:idx + 1])))
                idx -= 5
            idx -= 1
        return ', '.join(pattern)

    result = ''
    for i in n:
        result += st_val[st.index(i)]
    return findpattern(result)


password = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']
st = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
st_val = [0]*len(st)
for i in range(len(st)):
    temp = ['0']*4
    cnt = 3
    num = i
    while cnt >= 0:
        temp[cnt] = str(num%2)
        cnt -= 1
        num //= 2
    st_val[i] = ''.join(temp)

a = '0DEC'
b = '0269FAC9A0'
print(binary(a))
print(binary(b))
