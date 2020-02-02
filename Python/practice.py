## arr의 배열을 선택정렬을 활용하여 숫자 크기대로 달팽이 모양(시계방향 회오리모양 안으로 수렴함)으로 정렬하시오.

arr = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]
result = [[0]*5]*5
sorting = []
b = [0, len(arr)-1, 0, len(arr[0])-1]  # 주어진 배열 크기의 상하좌우 끝 인덱스값을 표시 (boundary)
r = c = 0
x_direction = y_direction = 1
for i in arr: sorting += i
sorting.sort() # 여기까지는 arr을 1차원 배열로 정렬한 것

for n in sorting: # sorting에 정렬한 값을 하나씩 순차적으로 비어있는 result 2차 배열에 회오리 방향대로 입력하기
    print('a', result)
    result[r][c] = n
    if r == b[0]:  # 상
        if c == b[2]:  # 좌
            c_direction = 1
            b[2] += 1
        elif c == b[3]:
            r_direction = 1
            b[0] += 1
        else:
            c += 1
    elif r == b[1]:  # 하
        c -= 1
        if c == b[3]:
            c_direction = -1
            b[3] -= 1
        elif c == b[2]:
            r_direction = -1
            b[1] -= 1

print(result)
