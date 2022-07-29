T = int(input())

for _ in range(T):
    no = int(input())
    student = {}

    while len(student) < 10:
        line = input().split()

        for score in line:
            if score in student:
                student[score] += 1
            else:
                student[score] = 1

    result = sorted(student.items(), key=lambda x: (-int(x[1]), -int(x[0])))

    print(f"#{no}", result[0][0])