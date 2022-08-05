def check(n, n_list):
    if '5' in n:
        n_list[0] = n
        n_list[1] = n.replace('5', '6')
    if '6' in n:
        n_list[0] = n_list[0].replace('6', '5')


a, b = input().split()

a_56 = [0, 0]
b_56 = [0, 0]

check(a, a_56)
check(b, b_56)

for i in range(2):
    a_56[i] = int(a_56[i])
    b_56[i] = int(b_56[i])

print(a_56[0] + b_56[0], a_56[1] + b_56[1])