# 두 수 A, B 가 있고
# 두 수의 최대공약수, 최소공배수 : gcd, lcm 
# lcm = (A / gcd) * (B / gcd) * gcd 가 된다.
# A = a * gcd, B = b * gcd 가 되며 a 와 b 는 서로 서로소(coprime)이다.
# 이 때, 산술기하평균 공식에 대입해서 결론지으면 a + b >= 2 * sqrt(a * b) 이다.
# 두 수는 서로소라고 했으므로 같을 수 없기에 a + b > 2 * sqrt(a * b) 이 된다.
# 여기서 합의 최솟값을 찾는 것이므로 a * b 값을 구하고 a, b 를 찾으면 끝이 난다.
# 위 식을 통해서 a * b = lcm / gcd 를 알 수 있다.
# 문제에서 lcm, gcd 가 주어지므로 lcm / gcd 가 곧 구하고자 하는 두 수의 최솟값이 된다. 
# 따라서 lcm / gcd 의 약수 중 서로소인 것을 찾는다.
# 찾는 도중 두 수의 차이가 가장 작은 것, 즉 구간이 가장 짧은 것이 답이 된다.
# i 범위가 1 ~ sqrt(lcm / gcd) 이므로 i, (lcm / gcd) / i 를 구하게 된다.
# 반복문이 돌면서 i 값이 증가하면 할수록 (lcm / gcd) / i 도 점점 작아짐과 동시에 구간이 짧아진다.
# 최종적으로 마지막에 해당하는 수가 결국 구간이 가장 작은 값의 쌍이 되어 답이 된다.
# 답지 링크
# https://velog.io/@lacram/C-%EB%B0%B1%EC%A4%80-2436%EB%B2%88-%EA%B3%B5%EC%95%BD%EC%88%98
# 산술기하평균 링크
# https://bhsmath.tistory.com/266  

# 유클리드 호제법, 재귀함수를 이용해 최대공약수를 구하는 함수
def gcd(a, b):
    if not b:
        return a
    elif a < b:
        return gcd(a, b % a)
    else:
        return gcd(b, a % b)


n, m = map(int, input().split())

# lcm / gcd
m //= n

for i in range(1, int(m ** (1 / 2)) + 1):
    # (lcm / gcd) / i 
    if not m % i:
        # lcm / gcd = a * b 므로 현재 a 가 i 면 m // i 는 b 이다.
        # m = i * m // i 이기 때문이다.
        if gcd(i, m // i) == 1:
            ret = (i * n, (m // i) * n)

print(ret[0], ret[1])