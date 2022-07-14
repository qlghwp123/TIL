# 1. defaultdict

from collections import defaultdict

S = input()
count = defaultdict(int)

for i in S:
    count[i] += 1

for k, v in count.items():
    print(k, v)

#########################################

# 2. if ~ not in

S = input()
count = {}

for i in S:
    if i not in count:
        count[i] = 0
    count[i] += 1

for k, v in count.items():
    print(k, v)

##########################################

# 3. dict.setdefault()

S = input()
count = {}

for i in S:
    count.setdefault(i, 0)
    count[i] += 1

for k, v in count.items():
    print(k, v)