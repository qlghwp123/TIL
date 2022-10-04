# 장고 실행 흐름



## 1. 가상환경 및 django 설치 생략



## 2. articles app 생성



### 1. app 생성 

```bash
$ python manage.py startapp articles
```



### 2. app 등록

```python
# pjt/settings.py

"""
...
"""

# Application definition

INSTALLED_APPS = [
    # 'articles', 추가
    'articles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



### 3. urls.py 설정

```python
# pjt/urls.py

from django.urls import path, include

urlpatterns = [
    path('articles/', include('articles.urls')),
]
```

```python
# articles/urls.py

from django.urls import path
from . import views

# URL namespace 지정
app_name = 'articles'

# 각 CRUD URL 에 mapping 되는 URL dispatcher 설정
urlpatterns = [
    path('create/', views.create, name='create'),
    path('index/', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:pk>/delete', views.delete, name='delete'),
]
```



## 3. Model 

```python
# articles/models.py

from turtle import title
from django.db import models

'''
게시판 기능 
- 제목(20글자이내)
- 내용(긴 글)
- 글 작성시간/수정시간(자동으로 기록, 날짜/시간)
'''

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



## 4. CRUD 기능 구현

### 1. 게시글 생성



#### 	1. HTML Form 제공

```html
<!-- articles/create.html -->

{% extends 'base.html' %}

{% block content %}

<h1>글 쓰기</h1>

<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ article_form.as_p }}
    <input type="submit" value="글쓰기">
</form>

{% endblock %}
```




#### 	2. 입력 받은 데이터 처리

```python
# articles/views.py

"""
...
"""

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
```



### 2. 게시글 목록

```html
<!-- articles/index.html -->

{% extends 'base.html' %}

{% block content %}

<a href="{% url 'articles:create' %}">글 추가</a>

<hr />

{% for i in data %}
<h1>{{ i.title }}</h1>
<p>{{ i.created_at|date:'Y-m-d h:m:s' }} <span>{{ i.updated_at|date:'Y-m-d h:m:s' }}</span></p>
<p>{{ i.content }}</p>
<hr />
{% endfor %}

{% endblock %}
```

```python
# articles/views.py

"""
...
"""

def index(req):
    # 최신순으로 데이터를 조회하기 위해 id 의 역순으로 조회한다.
    data = Article.objects.all().order_by('-id')

    return render(req, 'articles/index.html', {'data': data})
```



### 3. 상세보기

```html
<!-- articles/detail.html -->

{% extends 'base.html' %}

{% block content %}

<h1>{{ article.title }}</h1>
<p>{{ article.created_at|date:'Y-m-d h:m:s' }} <span>{{ article.updated_at|date:'Y-m-d h:m:s' }}</span></p>
<p>{{ article.content }}</p>
<p><a href="{% url 'articles:update' article.id %}">수정</a>
    <a href="{% url 'articles:delete' article.id %}">삭제</a>
    <a href="{% url 'articles:index' %}">목록</a>
</p>
<hr />

{% endblock %}
```

```python
# articles/views.py 

"""
...
"""

def detail(req, _id):
    # 파라미터로 넘겨받은 데이터를 이용해서 어느 데이터인지 찾는다.
    article = Article.objects.get(id=_id)

    return render(req, 'articles/detail.html', {'article': article})
```



### 4. 수정하기

```html
<!-- articles/update.html -->

{% extends 'base.html' %}

{% block content %}

<h1>글 수정하기</h1>

<form action="" method="POST">
    {% csrf_token %}
    {{ article_form.as_p }}
    <input type="submit" value="수정하기">
</form>

{% endblock %}
```

```python
# articles/views.py 

"""
...
"""

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
```



### 5. 삭제하기

```python
# articles/views.py 

"""
...
"""

def delete(req, _id):
    article = Article.objects.get(id=_id)

    article.delete()

    return redirect('articles:index')
```
