number = int(input())

cp = number
length = 0

while cp != 0:
    length += 1
    cp //= 10

cp = number
result = 0

while length > 0:
    result += (cp % 10) * (10 ** (length - 1))
    cp //= 10
    length -= 1 

print(result)