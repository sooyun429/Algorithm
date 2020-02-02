## 재평오빠 코드 참고
## k별로 구간을 정해서 max값을 찾고,
## max값들 중 최소값을 출력하면 징검다리를 건널 수 있는 최대 인원임
def solution(stones, k):
    res = max(stones)
    for i in range(k, len(stones), k):
        max_num = max(stones[i-k:i])
        if max_num < res:
            res = max_num
    return res

# ## 효율성 실패
# def solution(stones, k):
#     max_num = max(stones)
#     for i in range(max_num, -1, -1):
#         flag, cnt = 1, 0
#         for j in stones:
#             if j < i: cnt += 1
#             else: cnt = 0
#             print(i, j, cnt, flag)
#             if cnt >= k:
#                 flag = 0
#                 break
#         if flag:
#             max_num = i
#             break
#     return max_num


## 채점결과

# 테스트 1 〉	통과 (0.04ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.7MB)
# 테스트 3 〉	통과 (0.04ms, 10.7MB)
# 테스트 4 〉	통과 (0.05ms, 10.7MB)
# 테스트 5 〉	통과 (0.06ms, 10.8MB)
# 테스트 6 〉	통과 (2.06ms, 10.9MB)
# 테스트 7 〉	통과 (1.99ms, 10.8MB)
# 테스트 8 〉	통과 (2.12ms, 10.8MB)
# 테스트 9 〉	통과 (0.85ms, 10.8MB)
# 테스트 10 〉	통과 (0.12ms, 10.7MB)
# 테스트 11 〉	통과 (0.06ms, 10.8MB)
# 테스트 12 〉	통과 (0.17ms, 10.7MB)
# 테스트 13 〉	통과 (0.12ms, 10.7MB)
# 테스트 14 〉	통과 (0.76ms, 10.8MB)
# 테스트 15 〉	통과 (4.67ms, 10.8MB)
# 테스트 16 〉	통과 (0.79ms, 10.9MB)
# 테스트 17 〉	통과 (0.46ms, 10.9MB)
# 테스트 18 〉	통과 (0.06ms, 10.6MB)
# 테스트 19 〉	통과 (0.15ms, 10.7MB)
# 테스트 20 〉	통과 (0.34ms, 10.7MB)
# 테스트 21 〉	통과 (0.41ms, 10.7MB)
# 테스트 22 〉	통과 (8.28ms, 10.8MB)
# 테스트 23 〉	통과 (1.14ms, 10.8MB)
# 테스트 24 〉	통과 (1.26ms, 10.8MB)
# 테스트 25 〉	통과 (0.04ms, 10.8MB)


# # 첫 번째 시도
# def solution(stones, k):
#     answer = 0
#     while True:
#         flag = 1
#         for i in range(len(stones)):
#             if stones[i]:
#                 flag = 1
#                 stones[i] -= 1
#             else:
#                 flag += 1
#                 if flag > k:
#                     break
#         if flag > k:
#             break
#         answer += 1
#     return answer


## 채점 결과
# 테스트 1 〉	통과 (0.04ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.8MB)
# 테스트 3 〉	통과 (0.05ms, 10.7MB)
# 테스트 4 〉	통과 (0.09ms, 10.7MB)
# 테스트 5 〉	통과 (0.09ms, 10.7MB)
# 테스트 6 〉	통과 (23.10ms, 10.8MB)
# 테스트 7 〉	통과 (67.67ms, 10.9MB)
# 테스트 8 〉	통과 (77.91ms, 10.9MB)
# 테스트 9 〉	통과 (79.61ms, 10.8MB)
# 테스트 10 〉	통과 (0.11ms, 10.8MB)
# 테스트 11 〉	통과 (0.06ms, 10.7MB)
# 테스트 12 〉	통과 (0.14ms, 10.8MB)
# 테스트 13 〉	통과 (0.75ms, 10.7MB)
# 테스트 14 〉	통과 (24.78ms, 10.8MB)
# 테스트 15 〉	통과 (70.62ms, 10.9MB)
# 테스트 16 〉	통과 (77.40ms, 10.7MB)
# 테스트 17 〉	통과 (76.58ms, 10.8MB)
# 테스트 18 〉	통과 (0.10ms, 10.8MB)
# 테스트 19 〉	통과 (0.52ms, 10.7MB)
# 테스트 20 〉	통과 (1.61ms, 10.7MB)
# 테스트 21 〉	통과 (21.40ms, 10.9MB)
# 테스트 22 〉	통과 (54.76ms, 10.8MB)
# 테스트 23 〉	통과 (72.35ms, 10.8MB)
# 테스트 24 〉	통과 (78.48ms, 10.7MB)
# 테스트 25 〉	통과 (0.05ms, 10.8MB)



arr = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
jump = 3

print(solution(arr, jump))