N = int(input())
seats = input().split()
result = 0
for i in range(len(seats)):
    if seats[i] == '0':
        temp = N
        for j in range(i-1, -1, -1):
            if seats[j] == '1':
                if temp > i-j:
                    temp = i-j
                break
        for j in range(i+1, N):
            if seats[j] == '1':
                if temp > j-i:
                    temp = j-i
                break
        if temp > result:
            result = temp
print(result)
