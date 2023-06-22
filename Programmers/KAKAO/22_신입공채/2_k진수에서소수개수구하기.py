def solution(n, k):
    answer = 0 
    knum = ten2k(n, k)
    for candi in candidates(knum):
        if is_prime(candi):
            answer += 1
    return answer

def ten2k(n, k):
    s = ''
    while n > 0:
        n, rem = divmod(n, k)
        s += str(rem)
    return s[::-1]

def candidates(s):
    nums = s.split('0')
    return [int(num) for num in nums if num]

def is_prime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True