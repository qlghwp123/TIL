N = int(input())

logs = {}

for _ in range(N):
    line = input().split()
    if line[1] == "enter":
        logs[line[0]] = line[1]
    else: 
        del logs[line[0]]
        

logs = sorted(logs.items(), key=lambda x: x[0], reverse=True)

for person in logs:
    print(person[0])