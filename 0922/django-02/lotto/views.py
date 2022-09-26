from django.shortcuts import render
import random

# Create your views here.
def index(req):
    line_number = 5

    numbers = {}
    win = [3, 11, 15, 29, 35, 44]
    bonus = 10
    is_bonus = False

    for i in range(line_number):
        line = []
        
        for _ in range(6):
            line.append(random.randrange(1, 46))
        
        line.sort()

        cnt = 0
        for j in line:
            if j in win:
                cnt += 1
            if j == bonus:
                is_bonus = True

        if cnt == 6:
            line.append(1)
        elif cnt == 5:
            if is_bonus:
                line.append(2)
            else:
                line.append(3)
        elif cnt == 4:
            line.append(4)
        elif cnt == 3:
            line.append(5)
        else:
            line.append('꽝')

        numbers[i] = line

    return render(req, 'lotto.html', {'numbers': numbers})