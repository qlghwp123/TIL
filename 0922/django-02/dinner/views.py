from django.shortcuts import render
import random

# Create your views here.
def index(req):
    data = [
        ('삼겹살', 'http://www.hcnews.or.kr/img_up/shop_pds/hcnews/2022/pork-belly-g63b6ede64_6401646367594.jpg'),
        ('피자', 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Supreme_pizza.jpg/800px-Supreme_pizza.jpg'),
        ('치킨', 'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/202112/27/a99042fd-9510-42e9-97d6-6ae45ad666fc.jpg'),
        ('라면', 'https://cdn.mindgil.com/news/photo/202101/70570_6360_1754.jpg'),
        ('족발', 'https://w.namu.la/s/3c05b431f6a5e430a2b2db390a5b3b9ccd6ff8d823a05693a6d507d74b8b63ce794c733c0a0d46f6bf0dba35ddddef6c1593786a98beb539e80b781e18497c96a6a04335e4c11f648d526a2bc85d476df55680740c531507dfaa0be1af7eebea95ec064388c166dc02c22ba06b594eee')
    ]

    menu = random.choice(data)

    packet = {
        'name': menu[0],
        'link': menu[1]
    }

    return render(req, 'dinner.html', packet)