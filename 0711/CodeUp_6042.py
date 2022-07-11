a = float(input())

# VS Code python(3.8) 에서는 print(f"{a:.3}") 인데 코드업에서는 적용이 제대로 적용이 안되는거 같다.
# 알고 보니 소수점 자리 지정 숫자 옆에 f 을 붙이지 않으면 정상적인 동작이 안된다.
print(f"{a:.2f}")
#print(format(a, ".2f"))