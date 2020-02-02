import sys
sys.stdin = open('200129_naver ai burningday_03.txt', 'r')

# 1 0 1 0 1 1  # 1
# 1 1 0 1 1  # 2
# 0 1 0  # 0
# 0 1 1 0  # 2

for case in range(4):
    array = list(map(int, input().split()))
    temp1, temp2 = 0, 0
    for j in range(len(array)):
        if j%2:
            if array[j]:
                temp1 += 1
            else:
                temp2 += 1
        else:
            if array[j]:
                temp2 += 1
            else:
                temp1 += 1
    if temp1 > temp2:
        temp1 = temp2
    print(temp1)
