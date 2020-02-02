## 재평오빠 코드(수정함)
# [[0, 1], [0, 2], [3, 4], [3, 4]], [], visited, cur
def combination(mapping_idx, sel, visited, cur):
    global forbidden_id
    if cur == len(mapping_idx):
        tmp = sel[:]
        tmp.sort()
        if tmp not in forbidden_id:
            forbidden_id.append(tmp)
    else:
        for num in mapping_idx[cur]:
            if not visited[num]:
                visited[num] = 1
                sel.append(num)
                combination(mapping_idx, sel, visited, cur + 1)
                sel.pop()
                visited[num] = 0

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
# banned_id = ["fr*d*", "*rodo", "******", "******"]

forbidden_id =[]
mapping_idx = [[] for _ in range(len(banned_id))]

for bdx in range(len(banned_id)):
    length = len(banned_id[bdx])
    for udx in range(len(user_id)):
        if len(user_id[udx]) == length:
            for i in range(length):
                if banned_id[bdx][i] != '*' and banned_id[bdx][i] != user_id[udx][i]: break
            else:  # for-else문 (for문이 끊기지 않고 다 돌면 실행함(flag를 두지 않아도 된다. python에서 쓰임))
                mapping_idx[bdx].append(udx)
# print(mapping_idx)

combination(mapping_idx, [], [0]*len(user_id), 0)
print(forbidden_id)
print(len(forbidden_id))


# ## 재평오빠 코드(원본)

# def combination(mapping_idx, sel, visited, cur):
#     global forbidden_id
#     if cur == len(mapping_idx):
#         tmp = sel[:]
#         tmp.sort()
#         if tmp not in forbidden_id:
#             forbidden_id.append(tmp[:])
#     else:
#         for num in mapping_idx[cur]:
#             if not visited[num]:
#                 visited[num] = 1
#                 sel.append(num)
#                 combination(mapping_idx, sel, visited, cur + 1)
#                 sel.pop()
#                 visited[num] = 0

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# # banned_id = ["*rodo", "*rodo", "******"]
# banned_id = ["fr*d*", "*rodo", "******", "******"]

# forbidden_id =[]
# mapping_idx = []

# for bdx in range(len(banned_id)):
#     tmp = []
#     length = len(banned_id[bdx])
#     for udx in range(len(user_id)):
#         if len(user_id[udx]) == length:
#             for i in range(length):
#                 if banned_id[bdx][i] == '*':
#                     continue
#                 elif banned_id[bdx][i] != user_id[udx][i]:
#                     break
#             else:
#                 tmp.append(udx)
#     mapping_idx.append(tmp)
# print(mapping_idx)

# combination(mapping_idx, [], [0]*len(user_id), 0)
# print(forbidden_id)
# print(len(forbidden_id))

## 시도하다가 멈춤

# cnt = 0

# def comb(arr, used):
#     global cnt
#     # print('used', used)
#     for i in range(len(used[0])):
#         # print(used[0][i])
#         if used[0][i]:
#             arr.append(used[0][i])
#             used[0][i] = 0
#             if len(used) > 1:
#                 comb(arr, used[1:])
#             else:
#                 cnt += 1
#                 return

# def solution(user_id, banned_id):
#     answer = 1
#     answer_list = [[] for _ in range(len(banned_id))]
#     cnt = 1
#     for i in range(len(banned_id)):
#         b = banned_id[i]
#         for j in range(len(user_id)):
#             u = user_id[j]
#             if len(u)==len(b):
#                 flag = True
#                 for k in range(len(b)):
#                     if b[k] != '*' and b[k] != u[k]:
#                         flag = False
#                         break
#                 if flag:
#                     answer_list[i].append(j+1)
#     print(answer_list)
#     comb([], answer_list)
#     return cnt
# id_list = ["frodo","fradi","crodo","abc123","frodoc"]
# aa = ["fr*d*","abc1**"]
# bb = ["*rodo","*rodo","******"]
# cc = ["fr*d*","*rodo","******","******"]
# print(solution(id_list, aa)) #2
# print(solution(id_list,bb)) # 2
# print(solution(id_list,cc)) # 3


# ## 원래 코드

# def solution(user_id, banned_id):
#     answer = 1
#     big_flag = 0
#     answer_list = [[] for _ in range(len(banned_id))]
#     for i in range(len(banned_id)):
#         b = banned_id[i]
#         N = len(b)
#         for u in user_id:
#             if len(u)==N:
#                 flag = 1
#                 for i in range(N):
#                     if b[i] != '*' and b[i] != u[i]:
#                         flag = 0
#                         break
#                 if flag:
#                     big_flag = 1
#                     cnt += 1
#         if cnt:
#             answer *= cnt
#     if big_flag ==0:
#         answer = 0
#     return answer


# id_list = ["frodo","fradi","crodo","abc123","frodoc"]
# aa = ["fr*d*","abc1**"]
# bb = ["*rodo","*rodo","******"]
# cc = ["fr*d*","*rodo","******","******"]
# print(solution(id_list, aa)) #2
# print(solution(id_list,bb)) # 2
# print(solution(id_list,cc)) # 3


