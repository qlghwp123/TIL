# 이 문제는 딱히 할 말이 없다. 그냥 문제 그대로 구현 가능하다.
l = list(map(int, input().split()))

ascending = [i for i in range(1, 9)]
descending = sorted(ascending, reverse=True)

if l == ascending:
    print("ascending")
elif l == descending:
    print("descending")
else:
    print("mixed")