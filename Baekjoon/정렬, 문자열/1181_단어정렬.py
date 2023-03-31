n = int(input())
word_set = set()

for _ in range(n):
    word_set.add(input())

word_li = list(word_set)
result = sorted(word_li, key=lambda x : (len(x), x))

for i in result:
    print(i)