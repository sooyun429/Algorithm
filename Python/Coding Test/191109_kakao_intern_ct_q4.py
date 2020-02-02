## 재평오빠 코드 (재귀함수, sys.setrecursionlimit 사용)
import sys
sys.setrecursionlimit(10**6)


def union(visited, need_number):
    if visited.get(need_number):
        visited[need_number] = union(visited, visited[need_number])
        return visited[need_number]
    else:
        visited[need_number] = need_number + 1
        return need_number
        
k = 10
room_number = [1,3,4,1,3,1]

visited = {}

for idx in range(len(room_number)):
    room_number[idx] = union(visited, room_number[idx])
    # while 1:
    #     if visited.get(need_number):
    #         visited[need_number] += 1
    #         need_number = visited[need_number]
    #     else:
    #         visited[need_number] = need_number
    #         answer[idx] = need_number
    #         break
    print(visited)
print(room_number)



## 효율성 실패
# def solution(k, room_number):
#     empty = [1]*(k+1)
#     for n in range(len(room_number)):
#         number = room_number[n]
#         if empty[number]: empty[number] = 0
#         else:
#             for i in range(number+1, k+1):
#                 if empty[i]:
#                     room_number[n] = i
#                     empty[i] = 0
#                     break
#     return room_number


# ## 채점 결과
# 테스트 1 〉	통과 (0.04ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.7MB)
# 테스트 3 〉	통과 (0.04ms, 10.7MB)
# 테스트 4 〉	통과 (0.14ms, 10.8MB)
# 테스트 5 〉	통과 (0.05ms, 10.6MB)
# 테스트 6 〉	통과 (0.06ms, 10.7MB)
# 테스트 7 〉	통과 (0.05ms, 10.7MB)
# 테스트 8 〉	통과 (0.04ms, 10.8MB)
# 테스트 9 〉	통과 (0.04ms, 10.7MB)
# 테스트 10 〉	통과 (0.05ms, 10.8MB)
# 테스트 11 〉	통과 (0.06ms, 10.6MB)
# 테스트 12 〉	통과 (0.05ms, 10.8MB)
# 테스트 13 〉	통과 (0.04ms, 10.7MB)
# 테스트 14 〉	통과 (0.07ms, 10.6MB)
# 테스트 15 〉	통과 (0.07ms, 10.6MB)
# 테스트 16 〉	통과 (0.08ms, 10.7MB)
# 테스트 17 〉	통과 (0.08ms, 10.7MB)
# 테스트 18 〉	통과 (0.18ms, 10.8MB)
# 테스트 19 〉	통과 (0.24ms, 10.8MB)
# 테스트 20 〉	통과 (0.34ms, 10.8MB)
# 테스트 21 〉	통과 (0.84ms, 10.8MB)
# 테스트 22 〉	통과 (0.78ms, 10.9MB)
# 테스트 23 〉	통과 (0.47ms, 10.9MB)
# 테스트 24 〉	통과 (0.82ms, 11MB)
# 테스트 25 〉	통과 (0.05ms, 10.8MB)
# 테스트 26 〉	통과 (0.09ms, 10.7MB)