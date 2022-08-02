import sys

input = sys.stdin.readline

T = int(input())

people = {}
count = 0
for _ in range(T):
    line = input().strip()
    if line != "ENTER":
        if line not in people:
            people[line] = 1
            count += 1
    else:
        people = {}

print(count)