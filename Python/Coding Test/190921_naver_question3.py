# 이중 list의 sorting 테스트
test = [[4,2], [6,7,5], [3,4,9]]
test.sort()
print(test)

def solution(data):
    N = len(data)
    waiting_list = []
    # used = [0]+[1]*(N-1)
    result = [data[0][0]]
    time = data[0][1]+data[0][2]
    data.pop(0)
    while data or waiting_list:
        for i in range(len(data)-1, -1, -1):
            if data[i][1] <= time:
                # 3-1. 대기 중인 문서중 페이지 수가 적은 문서부터 인쇄합니다.
                # waiting_list에 있는 것들 중 페이지 수가 적은 문서 먼저 인쇄
                # sort 사용하기 위해 페이지수 정보를 맨 앞으로 가져오도록 순서를 바꾼다.
                waiting_list += [[data[i][2], data[i][1], data[i][0]]]
                data.pop(i)
        if waiting_list==[]:
            time = data[0][1]+data[0][2]
            result += [data[0][0]]
            data.pop(0)
        else:
            # 3-2. 대기 중인 문서중 페이지 수가 같은 문서가 있을 경우, 먼저 요청된 문서부터 인쇄합니다.
            waiting_list.sort()
            idx, min_doc = 0, waiting_list[0][2]
            for i in range(1, len(waiting_list)):
                # 대기 중 문서에서 가장 적은 페이지 수의 문서가 여러 개인 경우
                if waiting_list[i][0] == waiting_list[0][0]:
                    if waiting_list[i][2] < min_doc:
                        idx, min_doc = i, waiting_list[i][2]
                else:
                    break
            time += waiting_list[idx][0]
            result += [waiting_list[idx][2]]
            waiting_list.pop(idx)
    return result


## 실제 시험 제출 답안
# def solution(data):
#     N = len(data)
#     start = 100000000
#     for i in range(N):
#         if data[i][1] < start:  # data 입력값은 오름차순으로 주어지므로 사전 검증할 필요 없음
#             start = data[i][1]
#         data[i][0], data[i][2] = data[i][2], data[i][0]  # 문서번호와 페이지 수 순서를 바꿔줬었는데.. 이것도 더 효율적으로 수정할 수 있을 것 같다.
#     data.sort()
#     used = [1] * N
#     time = start
#     for i in range(N):
#         if data[i][1] == time:
#             answer = [data[i][2]] # 첫 번 째 문서 번호 정답리스트에 넣기
#             time += data[i][0] # 첫 문서 작업 끝나는 시간으로 수정(작업시간 더해주기)
#             used[i] = 0  # 첫 문서 사용했음을 표시하기
#             break  # 여기까지의 과정을 훨씬 간단하게 줄일 수 있음
#     while sum(used):
#         check = 1
#         for i in range(N):
#             # 끝나는 시간(time) 내에 요청시간이 있으면서 사용한 적이 없는 문서를 result에 넣는다(조건에 만족하지 않아서 답이 틀림)
#             # 구멍은 여기에 있음...
#             if data[i][1] <= time and used[i]: 
#                 answer.append(data[i][2])
#                 time += data[i][0]
#                 used[i] = 0
#                 check = 0
#                 break
#         if check:
#             for i in range(N):
#                 if used[i]:
#                     answer.append(data[i][2])
#                     time = data[i][1] + data[i][0]
#                     used[i] = 0
#                     break

#     return answer


a = [[1, 0, 5],[2, 2, 2],[3, 3, 1],[4, 4, 1],[5, 10, 2]]	# [1,3,4,2,5]
b = [[1, 0, 3], [2, 1, 3], [3, 3, 2], [4, 9, 1], [5, 10, 2]]	# [1,3,2,4,5]
c = [[1, 2, 10], [2, 5, 8], [3, 6, 9], [4, 20, 6], [5, 25, 5]]	# [1,2,4,5,3]
print(solution(a))
print(solution(b))
print(solution(c))