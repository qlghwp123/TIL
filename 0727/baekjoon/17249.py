# 태보의 조건은 결국 골뱅이 개수만 탐지하면 된다.
taebo = input().split("(^0^)")

print(taebo[0].count('@'), taebo[1].count('@'))