def solution(user_id, banned_id):
    from itertools import product
    answer = []
    for i in range(len(banned_id)):
        my_list = []
        for j in range(len(user_id)):
            count = 0
            for k in range(len(banned_id[i])):
                if len(banned_id[i]) == len(user_id[j]):
                    if banned_id[i][k] == user_id[j][k] or banned_id[i][k] == '*':
                        count += 1
            if count == len(user_id[j]):
                my_list.append(user_id[j])
        answer.append(my_list)
    answer = list(map(set, product(*answer)))  # itertools product 사용법!!
    # set을 사용한 이유는 {0, 1, 2, 2}와 같은 경우에 같은 원소가 있는 걸 없애주기 위해서
    # 그런데 set을 쓰게 되면 원소가 중복되는 경우 삭제되므로 length 체크가 필요하게 된다(banned 아이디의 갯수만큼 있어야 하므로)
    # 그래서 아래처럼 len 체크를 해주고, not in을 써서 이미 result에 있는 값은 제외해준다.
    # set은 집합개념이라서 순서와 상관없이 원소의 종류가 같으면 같은 set이라고 판단한다(sorting할 필요 없음)
    print(answer)
    result = []
    for ans in range(len(answer)):
        if len(answer[ans]) == len(banned_id) and answer[ans] not in result:
            result.append(answer[ans])
    return len(result)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
# banned_id = ["fr*d*", "*rodo", "******", "******"]

print(solution(user_id, banned_id))