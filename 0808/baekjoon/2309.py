height = [int(input()) for _ in range(9)]

for i in range(9):
    for j in range(8):
        temp = list(height)
        temp.remove(temp[i])
        temp.remove(temp[j])

        if sum(temp) == 100:
            break
    if sum(temp) == 100:
        break

print(*sorted(temp))