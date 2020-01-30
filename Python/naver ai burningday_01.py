import sys, itertools
sys.stdin = open('naver ai burningday_01.txt', 'r')

# def concat(input_arr, temp_arr):
#     global res
#     flag = 0
#     for i in input_arr:
#         for j in temp_arr:
#             if i not in j:
#                 for k in i:
#                     if k in j:
#                         break
#                 else:
#                     temp = [i+j, j+i]
#                     temp_arr += temp
#                     flag = 1
#                     if len(temp[0]) > res:
#                         res = len(temp[0])
#     if flag==0:
#         return res
#     else:
#         concat(input_arr, temp_arr)

## 두 번째 시도 (성공)
# for case in range(4):
#     A = list(map(str, input().split()))
#     print(A)
#     array = ['']
#     res = 0
#     for word in A[::-1]: # 사전에 A 배열 글자중 중복된 글자들이 들어있는 값을 제거
#         for char in word:
#             if word.count(char)>1:
#                 A.pop(A.index(word))
#                 break
#     # concat(A, [''])
#     while True:
#         flag = len(array)
#         for i in A:
#             for j in array:
#                 if i not in j:
#                     temp = [i+j, j+i]
#                     for word in temp:
#                         for char in word:
#                             if word.count(char) > 1:
#                                 break
#                         else:
#                             if word not in array:
#                                 array += [word]
#                                 if len(word) > res:
#                                     res = len(word)
#         print(array)
#         if len(array) == flag:
#             break
#     print(array)
#     print(res)

## itertools 사용
# for case in range(4):
#     A = list(map(str, input().split()))
#     print(A)
#     array = []
#     for num in range(len(A)):
#         array += list(itertools.combinations(A, num))
#     print(array)
#     res = 0
#     for word in array:
#         temp = ''.join(word)
#         for char in temp:
#             if temp.count(char) > 1:
#                 break
#         else:
#             if len(temp) > res:
#                 res = len(temp)
#     print(res)

# 현지 풀이 (itertools)
for case in range(4):
    A = list(map(str, input().split()))
    # t = [0]*depth
    for depth in range(len(A)-1, -1, -1): # 길이가 긴 최대의 경우를 찾아내면 되므로 index 거꾸로 접근
        candis = list(itertools.combinations(A, depth))
        print(candis) # [('co', 'dil'), ('co', 'ity'), ('dil', 'ity')]
        # codil과 dilco를 별도로 분석할 필요 없음(글자최대길이만 찾아내면 되니까)
        for can in candis: # can은 ('co', 'dil')
            once = []
            for c in can: # c는 co
                flag = True
                for i in c: # i는 c, o
                    if i not in once:
                        once.append(i)
                    else:
                        flag = False
                        break
                if not flag:
                    break
            else:
                print(once)
                print(len(once))
                break
                # return len(once)
    # return 0


# # 현지 풀이 (itertools) 수정
# for case in range(4):
#     A = list(map(str, input().split()))
#     # t = [0]*depth
#     for depth in range(len(A)-1, -1, -1): # 길이가 긴 최대의 경우를 찾아내면 되므로 index 거꾸로 접근
#         candis = list(itertools.combinations(A, depth))
#         # print(candis) # [('co', 'dil'), ('co', 'ity'), ('dil', 'ity')]
#         # codil과 dilco를 별도로 분석할 필요 없음(글자최대길이만 찾아내면 되니까)
#         for can in candis: # can은 ('co', 'dil')
#             once = []
#             for c in can: # c는 co
#                 for i in c: # i는 c, o
#                     if i in once:
#                         break
#                     once.append(i)
#                 else:
#                     continue
#                 break
#             else:
#                 # print(once)
#                 print(len(once))
#                 break
#                 # return len(once)
#     # return 0