def solution(nums):
    # 중복제거한 종류 수
    answer = len(set(nums))  

    # 최대 선택가능 수(N/2)가 더 작은 경우
    if answer > len(nums)/2:
        return len(nums)/2

    return answer

print(solution([3,1,2,3]))