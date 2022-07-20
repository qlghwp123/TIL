T = int(input())

for i in range(T):
    val = input()

    month = val[4:6]
    day = val[6:8]
    days = [False, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if not (0 < int(month) < 13):
        print(f"#{i + 1}", -1)
        continue
    
    if not (0 < int(day) < days[int(month)] + 1):
        print(f"#{i + 1}", -1)
        continue
    
    result = val[:4] + "/" + month + "/" + day

    print(f"#{i + 1}", result)