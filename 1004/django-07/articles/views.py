from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def create(req):
    # 요청이 POST 
    if req.method == 'POST':
        # POST 의 경우 ModelForm 생성자에 request.POST 를 넣는다.
        article_form = ArticleForm(req.POST)

        # 입력이 제대로 들어왔는지 유효성 검사
        if article_form.is_valid():
            # 입력이 제대로 들어왔으면 저장
            article_form.save()

            return redirect('articles:index')
    else:
        # 요청이 GET 이므로 html 태그를 구성하는 데이터를 만든다.
        article_form = ArticleForm()

    return render(req, 'articles/create.html', {'article_form': article_form})


def index(req):
    # 최신순으로 데이터를 조회하기 위해 id 의 역순으로 조회한다.
    data = Article.objects.all().order_by('-id')

    return render(req, 'articles/index.html', {'data': data})


def detail(req, _id):
    # 파라미터로 넘겨받은 데이터를 이용해서 어느 데이터인지 찾는다.
    article = Article.objects.get(id=_id)

    return render(req, 'articles/detail.html', {'article': article})


def update(req, _id):
    # 파라미터로 넘겨받은 데이터를 이용해서 어느 데이터인지 찾는다.
    article = Article.objects.get(id=_id)

    # 요청이 POST 
    if req.method == 'POST':
        # POST 의 경우 ModelForm 생성자에 request.POST 를 넣는다.
        # 그리고 위에서 찾은 데이터를 특정하기 위해 
        # instance 라는 이름의 keyword argument 를 사용한다.
        article_form = ArticleForm(req.POST, instance=article)

        # 입력이 제대로 들어왔는지 유효성 검사
        if article_form.is_valid():
            # 입력이 제대로 들어왔으면 저장
            article_form.save()

            return redirect('articles:detail', _id)

    else:
        # 요청이 GET 이므로 html 태그를 구성하는 데이터를 만든다.
        # 단, 여기서 detail 내 update 므로 반드시 위에서 찾은 데이터로
        # 넘기기 위해 마찬가지로 instance 라는 이름의 keyword argument 를 사용한다.
        article_form = ArticleForm(instance=article)

    return render(req, 'articles/update.html', {'article_form': article_form})


def delete(req, _id):
    article = Article.objects.get(id=_id)

    article.delete()

    return redirect('articles:index')