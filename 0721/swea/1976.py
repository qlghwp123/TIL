T = int(input())

for i in range(T):
    time_list = list(map(int, input().split()))

    hour = time_list[0] + time_list[2]
    minute = time_list[1] + time_list[3]

    exceed = True if (minute > 59) else False
    carry = 1 if exceed else 0

    minute = minute - 60 if exceed else minute
    hour += carry
    hour = hour - 12 if hour > 12 else hour 

    print(f"#{i + 1}", hour, minute)