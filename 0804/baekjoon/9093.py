# sys.stdin.readline 유무는 실행 시간이 600ms 차이를 가져왔다.
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    line = input().split()
    
    for word in line:
        print(word[::-1], end=' ')
    
    print()