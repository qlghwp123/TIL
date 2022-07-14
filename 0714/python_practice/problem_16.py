S = input()
vowel = list("aeiou")
count = 0
for alpha in S:
    if alpha in vowel:
        count += 1
print(count)