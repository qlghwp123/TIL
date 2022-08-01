import sys

input = sys.stdin.readline

duck = ["제", "리"]
line = input().strip()[-1]
count = 0

while line != "끝":
    if line == duck[0]:
        count += 1
    elif line == duck[1]:
        count = count - 1 if count > 0 else 2
    
    line = input().strip()[-1]

print("힝구" if count else "고무오리야 사랑해")