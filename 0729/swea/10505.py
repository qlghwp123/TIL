T = int(input())

for i in range(T):
    N = int(input())

    income_list = list(map(int, input().split()))
    mean = sum(income_list) // len(income_list)
    result = list(filter(lambda x: x <= mean, income_list))

    print(f"#{i + 1}", len(result))