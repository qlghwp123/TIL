from django.shortcuts import render

# Create your views here.
def is_odd_even(req, val):
    return render(req, 'is-odd-even.html', {'val': int(val), 'ret': int(val) % 2 == 0})