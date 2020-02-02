import sys
sys.stdin = open('200129_naver ai burningday_02.txt', 'r')

for case in range(3):
    # array = list(input())
    # # print(array)
    # length = len(array)
    # front = 0
    # res = ''
    # while front < length//2:
    #     back = -1-front
    #     if array[front] == '?' or array[back] == '?':
    #         if array[front] != '?':
    #             array[back] = array[front]
    #         elif array[back] != '?':
    #             array[front] = array[back]
    #         else:
    #             array[front] = 'a'
    #             array[back] = 'a'
    #     else:
    #         if array[front] != array[back]:
    #             res = 'NO'
    #             break
    #     front += 1
    # if res == '':
    #     res = ''.join(array)
    # print(res)

## 현지의 solution
# def solution(S):
#     temp = list(S)
    temp = list(input())
    res = ''

    result = [0]*len(temp)

    for i in range(len(temp)//2):
        if (temp[i]=="?") or (temp[len(temp)-1-i]=="?"):
            if temp[i] == temp[len(temp)-1-i]:
                result[i] = 'a'
                result[len(temp)-1-i] = 'a'
            elif temp[i] == "?":
                result[i] = temp[len(temp)-1-i]
                result[len(temp)-1] = result[i]
            elif temp[i] != "?":
                result[i] = temp[i]
                result[len(temp)-1-i] = temp[i]
        elif (temp[i]==temp[len(temp)-1-i]):
            result[i] = temp[i]
            result[len(temp)-1-i] = temp[i]
        else:
            # return "NO"
            res = 'NO'
            print(res)
            break
    if res == '':
        if len(temp) % 2:
            result[len(temp)//2] = ''.join(temp)[len(temp)//2]  # 글자 수가 홀수개인 경우 가운데 글자 추가해주기

        # return ''.join(result)
        print(''.join(result))