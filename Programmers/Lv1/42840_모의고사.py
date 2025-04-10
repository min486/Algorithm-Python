def solution(answers):    
    num_one = [1, 2, 3, 4, 5]
    num_two = [2, 1, 2, 3, 2, 4, 2, 5]
    num_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    li_cnt = [0, 0, 0]
    for idx, i in enumerate(answers):
        if i == num_one[idx % len(num_one)]:
            li_cnt[0] += 1
        if i == num_two[idx % len(num_two)]:
            li_cnt[1] += 1
        if i == num_three[idx % len(num_three)]:
            li_cnt[2] += 1
            
    mx = max(li_cnt)
    ans = []
    for idx, j in enumerate(li_cnt):
        if j == mx:
            ans.append(idx+1)
            
    return ans