val = list(input())

for i in val:
    print(ord(i) - ord('A') + 1, end=' ')