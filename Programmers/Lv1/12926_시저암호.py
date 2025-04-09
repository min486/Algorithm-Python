def solution(s, n):
    answer = ''
    for ch in s:
        if ch == ' ':
            answer += ' '
        else:
            if ch.isupper():
                num = ord(ch) + n
                if 65 <= num <= 90:
                    ch = chr(num)
                else:
                    ch = chr(num-26)
            elif ch.islower():
                num = ord(ch) + n
                if 97 <= num <= 122:
                    ch = chr(num)
                else:
                    ch = chr(num-26)
            answer += ch
    
    return answer