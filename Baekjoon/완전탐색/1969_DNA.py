n, m = map(int, input().split())
dna = []

for _ in range(n):
    dna.append(input())
    
result_dna = ''
result_cnt = 0

for i in range(m):
    # A, C, G, T 개수
    acgt_cnt = [0, 0, 0, 0]  
    # 가장 많이 나온 문자 -> dna
    for j in range(n):
        if dna[j][i] == 'A':
            acgt_cnt[0] += 1
        elif dna[j][i] == 'C':
            acgt_cnt[1] += 1
        elif dna[j][i] == 'G':
            acgt_cnt[2] += 1
        elif dna[j][i] == 'T':
            acgt_cnt[3] += 1
    idx = acgt_cnt.index(max(acgt_cnt))

    if idx == 0:
        result_dna += 'A'
    elif idx == 1:
        result_dna += 'C'
    elif idx == 2:
        result_dna += 'G'
    elif idx == 3:
        result_dna += 'T'
    # 가장 많이 나온 문자 제외한 문자 개수
    result_cnt += n - max(acgt_cnt)

print(result_dna)
print(result_cnt)