T = int(input())

for i in range(T):
    s = list(input())

    result = 1
    for j in range(len(s)//2):
        if s[j] != s[-(j + 1)]:
            result = 0
            break
    # if s != s[::-1]:
    #     result = 0

    print(f"#{i + 1}", result)