T = input()

for i in range(T):
    line = input()

    # 마디 길이 최대가 10
    for j in range(10):
        line.index(line[:i], i)

    print(f"#{i + 1}", )