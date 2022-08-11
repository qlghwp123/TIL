import sys

input = sys.stdin.readline

K, S, N = input().rstrip().split()

# T 가 행을 증가시키고
# B가 행을 감소시킴
move = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (-1, 0),
    "T": (1, 0),
    "RT": (1, 1),
    "LT": (1, -1),
    "RB": (-1, 1),
    "LB": (-1, -1)
}

# 순서를 바꿈.
K = int(K[1]) - 1, ord(K[0]) - 65 
S = int(S[1]) - 1, ord(S[0]) - 65

for _ in range(int(N)):
    i, j = move[input().rstrip()]

    if -1 < K[0] + i < 8 and -1 < K[1] + j < 8:
        if K[0] + i == S[0] and K[1] + j == S[1]:
            if -1 < S[0] + i < 8 and -1 < S[1] + j < 8:
                K = S[0], S[1]
                S = S[0] + i, S[1] + j
            else:
                continue
        else:
            K = K[0] + i, K[1] + j
    else:
        continue

# 다시 순서 바꿔서 처리
print(chr(K[1] + 65) + str(K[0] + 1), chr(S[1] + 65) + str(S[0] + 1), sep='\n')
