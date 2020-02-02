
# arr의 부분집합 중 합이 0인 경우의 수 모두 출력하시오.
arr = [1, 5, -9, 6, -2, 1, 2, 3, 4, 5]
result = []
for i in range(1, 1 << len(arr)):
    subset = []
    for j in range(len(arr)):
        if i & (1 << j):
            subset.append(arr[j])
    if sum(subset) == 0:
        result.append(subset)
print(len(result), result)


arr = [1, 5, -9, 6, -2]
for i in range(1, 1 << len(arr)):  # 첫 번째 range 안에  2**len(arr)을 넣는 것보다 1 << len(arr)을 넣는 것이 연산속도가 더 빠르다
    print(i)
    subset = []
    for j in range(len(arr)):
        print(j)
        if i & (1 << j):
            subset.append(arr[j])

    print(subset)



box = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
result = 0

big_box = [box[0]] + box + [box[-1]]
for i in range(len(big_box)):
    big_box[i] = [big_box[i][0]] + big_box[i] + [big_box[i][-1]]

for i in range(1, len(box)+1):
    for j in range(1, len(box[0])+1):
        result += abs(big_box[i][j]-big_box[i-1][j]) + abs(big_box[i][j]-big_box[i+1][j]) + abs(big_box[i][j]-big_box[i][j-1]) + abs(big_box[i][j] - big_box[i][j+1])

print(result)
#
for i in range(len(box)):
    for j in range(len(box[0])):
        if i == 0 and j == 0:
            result += abs(box[i][j] - box[i + 1][j]) + abs(box[i][j] - box[i][j + 1])
        elif i == 0 and j == len(box[0])-1:
            result += abs(box[i][j] - box[i + 1][j]) + abs(box[i][j] - box[i][j - 1])
        elif i == 0:
            result += abs(box[i][j] - box[i + 1][j]) + abs(box[i][j] - box[i][j - 1]) + abs(box[i][j] - box[i][j + 1])
        elif i == len(box)-1 and j == 0:
            result += abs(box[i][j] - box[i - 1][j]) + abs(box[i][j] - box[i][j + 1])
        elif i == len(box)-1 and j == len(box[0])-1:
            result += abs(box[i][j] - box[i - 1][j]) + abs(box[i][j] - box[i][j - 1])
        elif i == len(box)-1:
            result += abs(box[i][j] - box[i - 1][j]) + abs(box[i][j] - box[i][j - 1]) + abs(box[i][j] - box[i][j + 1])
        elif j == 0:
            result += abs(box[i][j] - box[i - 1][j]) + abs(box[i][j] - box[i + 1][j]) + abs(box[i][j] - box[i][j + 1])
        elif j == len(box[0])-1:
            result += abs(box[i][j] - box[i - 1][j]) + abs(box[i][j] - box[i + 1][j]) + abs(box[i][j] - box[i][j - 1])
        else:
            result += abs(box[i][j]-box[i-1][j]) + abs(box[i][j]-box[i+1][j]) + abs(box[i][j]-box[i][j-1]) + abs(box[i][j] - box[i][j+1])

print(result)