word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def solution(s):
    string = ''
    leng = 0

    while leng < len(s):
        if '0' <= s[leng] <= '9':
            string += s[leng]
            leng += 1
        else:
            for i in range(10):
                if s.find(word[i], leng, leng+5) != -1:
                    string += str(i)
                    leng += len(word[i])
                    break
                
    answer = int(string)
    return answer