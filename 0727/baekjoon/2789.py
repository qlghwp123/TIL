A = list(input())
censorship = list("CAMBRIDGE")
result = ""

# 문자열을 다 쪼개서 리스트로 넣고
# 해당 문자열을 순회하면서 체크한다.
for i in A:
    if i not in censorship:
        result += i

print(result)