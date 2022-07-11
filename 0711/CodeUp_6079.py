N = int(input())
answer = 0
i = 1

while True:
    if N <= answer:
        print(i-1)
        break

    answer += i
    i += 1