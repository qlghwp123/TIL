S = input()

for i in range(1, 16):
    print(S + f"*{i:X}={(ord(S)-55)*i:X}")