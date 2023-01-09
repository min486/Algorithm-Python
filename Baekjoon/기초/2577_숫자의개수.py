li = []
for _ in range(3):
    li.append(int(input()))
    
abc = str(li[0] * li[1] * li[2])

for i in range(10):
    print(abc.count(str(i)))