# ref : https://www.acmicpc.net/board/view/75724
n, p, q = map(int, input().split())

a = {0:1}

def solution(n):
    if n in a:
        return a[n]
    else:
        a[n] = solution(n // p) + solution(n // q)
        return a[n]
        
print(solution(n))