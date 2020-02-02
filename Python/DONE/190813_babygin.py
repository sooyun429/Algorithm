num = 456789  # Baby Gin 확인할 6자리 수
c = [0] * 12  # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
tri = run = 0
num = list(str(num))
num.sort()
print(num)
for i in range(len(num)):
    if num.count(num[i]) >= 3:
        tri += 1
        for j in range(3):
            num.remove(num[i])
    if int(num[i]) + 1 == int(num[i+1]) and int(num[i+1]) + 1 == int(num[i+2]):
        run += 1
        for j in range(i+2, i-1, -1):
            num.remove(num[j])
if tri + run == 2:
    print('Baby Gin!')
else:
    print('Lose :(')



## teacher's answer
# for i in range(6):
#     c[num % 10] += 1
#     num //= 10
#
# i = 0
# tri = run = 0
#
# while i < 10:
#     if c[i] >= 3:  #triplet 조사 후 데이터 삭제
#         c[i] -= 3
#         tri += 1
#         continue;
#     if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:  # run 조사 후 데이터 삭제
#         c[i] -= 1
#         c[i+1] -= 1
#         c[i+2] -= 1
#         run += 1
#         continue
#     i += 1
#
# if run + tri == 2:
#     print('Baby Gin')
# else:
#     print('Lose')

