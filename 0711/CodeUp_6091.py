def gcd(a, b):
    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a

    while big % small:
        temp = big
        big = small
        small = temp % small

    return small

def lcm(a, b):
    return a * b // gcd(a, b)

    
l = list(set(map(int, input().split())))

first = lcm(l[0], l[1])

if len(l) == 1:
    print(l[0])
elif len(l) == 2:
    print(first)
else:
    print(lcm(first, l[2]))

# l = list(map(int, input().split()))
# d = 1
# while d%l[0]!=0 or d%l[1]!=0 or d%l[2]!=0 :
#   d += 1
# print(d)