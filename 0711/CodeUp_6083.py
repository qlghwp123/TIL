l = list(map(int, input().split()))

for i in range(l[0]):
    for j in range(l[1]):
        for k in range(l[2]):
            print(i, j, k, sep=" ")
            
print(l[0] * l[1] * l[2])