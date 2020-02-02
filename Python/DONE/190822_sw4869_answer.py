# def f(n):  # 재귀함수 사용
#     if n<2:
#         return 1
#     else:
#         return f(n-1) + s*f(n-2)
#
T = int(input())
l = [1, 1]
for i in range(2, 31):
    l.append(l[i-1] + 2*l[i-2])

for tc in range(1, T+1):
    N = int(input())//10
    print('#%d %d' % (tc, l[N]))