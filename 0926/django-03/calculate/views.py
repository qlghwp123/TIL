from django.shortcuts import render

# Create your views here.
def calculate(req, first, second):
    f = int(first)
    s = int(second)
    return render(req, 'calculate.html', {
        'first': f,
        'second': s,
        'add': f + s,
        'sub': f - s,
        'mul': f * s,
        'div': f // s
    })