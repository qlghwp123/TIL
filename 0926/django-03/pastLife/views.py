from django.shortcuts import render
import random

# Create your views here.
def past_life_input(req):
    return render(req, 'input.html')


def past_life(req):
    ret = random.choice('호랑이·토끼·용·뱀·말·소·원숭이·닭·돼지·개·쥐·양'.split('·'))

    return render(req, 'past-life.html', {'name': req.GET.get('name'), 'ret': ret})