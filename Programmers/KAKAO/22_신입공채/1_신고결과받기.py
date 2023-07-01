def solution(id_list, report, k):
    reportDic = {}  # 유저 ID : red ID
    resultDic = {}  # red ID : 유저 ID

    for re in report:
        user, red = re.split()
        if user not in reportDic:
            reportDic[user] = set()
        reportDic[user].add(red)

        if red not in resultDic:
            resultDic[red] = set()
        resultDic[red].add(user)

    answer = [0] * len(id_list)

    for i in range(len(id_list)):
        user = id_list[i]
        if user not in reportDic:  # 신고한적 없는 유저
            continue
        
        for red in reportDic[user]:  # 해당 유저가 신고한 red ID들에서
            if len(resultDic[red]) >= k:  # k번 이상 신고된 유저가 있으면
                answer[i] += 1  # 해당 유저에게 메일 발송 (+1)

    return answer