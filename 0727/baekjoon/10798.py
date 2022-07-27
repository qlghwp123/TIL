l = []

count = 0
for _ in range(5):
    temp = input()
    # 모든 줄의 길이 최댓값을 구한다.
    # 사실 문제를 읽어보니 최대가 15줄로 제한되어 있어서 이럴 필요는 없었다. 
    if count < len(temp):
        count = len(temp)
    l.append(temp)

result = ""

i = 0
while i < count:
    for j in range(5):
        # 세로로 읽으므로 첫 번째 인덱스가 움직인다.
        # 다만 증가하는 인덱스가 해당 줄의 크기보다 작아야한다.
        if i < len(l[j]):
            result += l[j][i]
    i += 1

print(result)