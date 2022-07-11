a, b, c = map(int, input().split())

print(c if ((b if a>b else a)>c) else (b if a>b else a)) 