def solution(array, commands):
    ans = []
    for li in commands:
        i = li[0]
        j = li[1]
        k = li[2]
        # 1. i~j 구간 자르기
        new_li = array[i-1 : j]
        # 2. 오름차순 정렬
        new_li.sort()
        # 3. k번째 수 구하기
        k = new_li[k-1]
        ans.append(k)
        
    return ans