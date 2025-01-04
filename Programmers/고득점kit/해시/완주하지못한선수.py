from collections import Counter
    
def solution(participant, completion):
    # 둘의 차를 구하면 정답만 남아있는 counter를 반환
    answer = Counter(participant) - Counter(completion)
    
    # counter의 key값을 반환
    # print(answer)
    # print(answer.keys())
    # print(list(answer.keys()))
    return list(answer.keys())[0]

# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))