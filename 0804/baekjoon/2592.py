from collections import Counter

l = []
for _ in range(10):
    l.append(int(input()))

print(sum(l) // 10, Counter(l).most_common(1)[0][0])