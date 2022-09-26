from django.shortcuts import render
import random

# Create your views here.
def lorem_input(req):
    return render(req, 'lorem_input.html')

def lorem_result(req):
    word_list = ['사과', '바나나', '짜장면', '짬뽕', '고수']
    
    para_cnt = int(req.GET.get('para-cnt'))
    word_cnt = int(req.GET.get('word-cnt'))

    ret = []

    for i in range(para_cnt):
        temp = []

        for j in range(word_cnt):
            temp.append(random.choice(word_list))

        ret.append(temp)

    return render(req, 'lorem_result.html', {'ret': ret})