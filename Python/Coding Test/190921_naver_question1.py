def solution(emails):
    answer = 0
    lowercase = '.abcdefghijklmnopqrstuvwxyz'
    toplevel = ['com', 'net', 'org']
    for email in emails:
        check = 0
        if email.count('@') == 1:
            name, domain = map(str, email.split('@'))
            if len(name) >= 1:
                for letter in name:
                    if letter not in lowercase:
                        check = 1
                        break
                if (not check) and domain.count('.') == 1:
                    part1, part2 = map(str, domain.split('.'))
                    if len(part1) >= 1 and (part2 in toplevel):
                        for letter in part1:
                            if letter not in lowercase[1:]:
                                check = 1
                                break
                        if not check:
                            answer += 1
    return answer