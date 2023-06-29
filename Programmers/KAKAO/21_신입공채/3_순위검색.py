from bisect import bisect_left

def solution(info, query):
    dic = {'-':0, 'cpp':1, 'java':2, 'python':3,
            'backend':1, 'frontend':2,
            'junior':1, 'senior':2,
            'chicken':1, 'pizza':2}
    
    arr = [[] for _ in range(4*3*3*3)]

    for string in info:
        st = string.split()
        tu = (dic[st[0]]*3*3*3,
            dic[st[1]]*3*3,
            dic[st[2]]*3,
            dic[st[3]])
        score = int(st[4])

        for i in range(1<<4):
            idx = 0
            for j in range(4):
                if i & (1 << j):
                    idx += tu[j]
            arr[idx].append(score)

    for i in range(4*3*3*3):
        arr[i] = sorted(arr[i])

    answer = []
    for string in query:
        st = string.split()
        idx = dic[st[0]]*3*3*3 + dic[st[2]]*3*3 + dic[st[4]]*3 + dic[st[6]]
        score = int(st[7])
        answer.append(len(arr[idx]) - bisect_left(arr[idx], score))

    return answer