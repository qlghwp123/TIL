N = int(input())

cards = list(map(int, input().split()))

M = int(input())

num_list = input().split()
numbers = dict.fromkeys(map(int, num_list), 0)

for card in cards:
    if card in numbers:
        numbers[card] += 1

for val in range(len(num_list)):
    key = int(num_list[val])
    print(numbers[key], end=' ')