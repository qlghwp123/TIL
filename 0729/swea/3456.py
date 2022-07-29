T = int(input())

for i in range(T):
    edge = list(map(int, input().split()))
    
    # 정렬하면 가운데는 항상 중복값
    edge.sort()

    print(f"#{i + 1}", edge[0] if edge[1] == edge[2] else edge[2])