S = input()
upper = []

for alpha in S:
    upper.append(chr(ord(alpha) - 32) if 97 <= ord(alpha) <= 122 else alpha)
        
print("".join(upper))