def check(ch):
    if ch.isalnum():
        return True
    if ch == '-' or ch == '_' or ch == '.':
        return True
    return False

def solution(new_id):
    answer = ''

    lastDot = False
    for ch in new_id:
        if check(ch) == False:  # 2단계
            continue

        if ch == '.':  # 3,4단계
            if len(answer) == 0 or lastDot:
                continue
            lastDot = True
        else:
            lastDot = False

        ch = ch.lower()  # 1단계
        answer += ch

    if len(answer) == 0:  # 5단계
        answer += 'a'

    if len(answer) >= 16:  # 6단계
        answer = answer[:15]

    if answer.endswith('.'):  # 6단계
        answer = answer[:-1]

    if len(answer) <= 2:  # 7단계
        end = answer[-1]
        while len(answer) < 3:
            answer += end

    return answer