import math
w, h = map(int, input().split())
x, y = map(int, input().split())
minnum = x+y
print(minnum)
result = math.factorial(minnum)//(math.factorial(x)*math.factorial(y))
print(result)
