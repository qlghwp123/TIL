number = int(input())

result = 0

while number != 0:
    result += number % 10
    number //= 10

print(result)