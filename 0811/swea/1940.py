T = int(input())

for i in range(1, T + 1):
    N = int(input())

    s, v, d = 0, 0, 0
    cmd, val = 0, 0

    for j in range(N):
        line = input()

        if ' ' in line:
            cmd, val = map(int, line.split())
        else:
            cmd, val = 0, 0
        
        if cmd == 1:
            v += val
        elif cmd == 2:
            if v >= val:
                v -= val
            else:
                val = 0

        d += v
        
    print(f"#{i}", d)