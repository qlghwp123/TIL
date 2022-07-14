S = input()
count = -1
for i in range(len(S)):
    if S[i] == 'a':
        count = i
        break
print(count)