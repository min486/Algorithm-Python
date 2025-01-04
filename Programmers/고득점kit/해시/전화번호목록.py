def solution(phone_book):
    # HashMap 생성
    hash_map = {}
    for key in phone_book:
        hash_map[key] = 1  # 전화번호 중복 없음
    
    # 접두어가 HashMap에 존재하는지 찾기
    for nums in phone_book:
        jubdoo = ""
        for num in nums:
            jubdoo += num
            # 접두어 찾기 (기존 번호와 같은 경우 제외)
            if jubdoo in hash_map and jubdoo != nums:
                return False
    return True

print(solution(["6", "12", "6789"]))