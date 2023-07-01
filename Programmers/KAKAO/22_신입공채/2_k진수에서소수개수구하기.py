def ten2k(n, k):
    st = ''
    while n > 0:
        n, rem = divmod(n, k)
        st += str(rem)
    return st[::-1]

def candidates(knum):
    numsLi = knum.split('0')
    return [int(num) for num in numsLi if num]

def is_prime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:  # 1이거나 짝수면 소수x
        return False
    for i in range(3, int(num**0.5) + 1, 2):  # 3, 5 .. num제곱근
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0 
    knum = ten2k(n, k)  # 10진수를 k진수로 변경
    for candi in candidates(knum):
        if is_prime(candi):
            answer += 1
    return answer