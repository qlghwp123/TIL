T = int(input())

mirror_alphabet = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p'
}

for i in range(T):
    line = list(input())

    result = line[::-1]

    for j in range(len(result)):
        result[j] = mirror_alphabet[result[j]]

    print(f"#{i + 1}", "".join(result))