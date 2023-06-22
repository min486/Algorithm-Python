def solution(id_list, report, k):
    reportDic = {}
    resultDic = {}

    for r in report:
        user, red = r.split()
        if user not in reportDic:
            reportDic[user] = set()
        reportDic[user].add(red)

        if red not in resultDic:
            resultDic[red] = set()
        resultDic[red].add(user)

    answer = [0 for _ in range(len(id_list))]

    for i in range(len(id_list)):
        user = id_list[i]
        if user not in reportDic:
            continue
        
        for red in reportDic[user]:
            if len(resultDic[red]) >= k:
                answer[i] += 1

    return answer