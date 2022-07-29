T = int(input())

start_number = {'3':0, '4':0, '5':0, '6':0, '9':0}

for i in range(T):
    line = list(filter(lambda x: x != '-', input()))
    result = 0

    if len(line) == 16 and line[0] in start_number:
        result = 1

    print(f"#{i + 1}", result)