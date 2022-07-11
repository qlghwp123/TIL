l = list(map(int, input().split()))

for i in l:
    (print("A") if not i % 2 else print("B")) if i < 0 else (print("C") if not i % 2 else print("D"))
