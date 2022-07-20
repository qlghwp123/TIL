T = int(input())

for i in range(T):
    P, Q, R, S, W = map(int, input().split())

    A = P * W
    B = Q if W <= R else Q + S * (W - R)

    if A > B:
        result = B
    else:
        result = A
    
    print(f"#{i + 1}", result)