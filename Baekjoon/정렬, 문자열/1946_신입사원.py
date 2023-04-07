t = int(input())

for _ in range(t):
    n = int(input())
    persons = [list(map(int, input().split())) for _ in range(n)]
    persons.sort()  # 서류 순위 기준 오름차순 정렬

    rank = persons[0][1]  # 첫번째 지원자의 면접 순위
    cnt = 1

    # 서류 성적은 다 떨어지므로 면접 성적 비교
    for i in range(1, n):
        # 지원자의 면접 순위가 전까지 저장된 가장 높은 순위보다 더 높을시 (숫자는 작아짐)
        if persons[i][1] < rank:  
            cnt += 1
            rank = persons[i][1]

    print(cnt)