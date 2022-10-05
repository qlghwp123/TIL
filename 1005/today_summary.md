# django - 08

* 각 앱의 admin 페이지를 설정하는 방법을 배웠다.

* django 에서 static 파일을 어떻게 관리하는지 배웠다.

* django-bootstrap5 패키지를 적용하는 법을 배웠다.

  

## admin 페이지 설정

* super user 생성

  ```bash
  $ python manage.py createsuperuser
  사용자 이름 (leave blank to use 'hypergrowth'): # 이름
  이메일 주소: # 생략가능
  Password: # 최소 8자리 이상
  Password (again): # 재입력
  ```

* 기본 제공하는 admin 페이지를 이용해 사용하고 있는 model 등록하기

  ```python
  # articles/admin.py
  
  from django.contrib import admin
  from .models import Article
  
  class ArticleAdmin(admin.ModelAdmin):
      # 반드시 리스트 또는 튜플이어야 한다.
      fields = ['title', 'content']
      # 조회 시 해당 필드의 값으로 제목 변경
      list_display = ['title', 'content']
  
  # 등록
  admin.site.register(Article)
  ```



## django 에서 static 파일 설정

* django 는 프로젝트 내에 templates 폴더가 하나 또는 여러 있으면 해당 이름의 폴더의 내용을 전부 읽어서 하나의 리스트로 만드는 형식과 같이 관리된다.

* (그래서 이 특징을 모를 경우 각 앱의 templates 폴더 내 같은 이름의 html 파일이 있으면 제대로 동작하지 않는다.)

* static 도 마찬가지이다. 프로젝트 내 정적 자원들의 위치(URL)를 정하는 부분이 settings.py 의 STATIC_URL 이다.

  ```python
  # pjt/settings.py
  
  """
  ...
  """
  
  # Application definition
  
  INSTALLED_APPS = [
      'articles',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles', # <- 이 녀석이 정적 파일을 관리한다.
  
  """
  ...
  """
  
  # default 값은 아래와 같다.
  
  # Static files (CSS, JavaScript, Images)
  # https://docs.djangoproject.com/en/3.2/howto/static-files/
  
  STATIC_URL = '/static/'
  ```

* 그리고 이를 활용하려면 DTL 에서 제공하는 문법을 따라야 한다.

* 그리고 해당 img 태그 src 속성 값을 보면 주소/static/ 으로 시작한다. 

  ```html
  <!-- articles/index.html -->
  
  <!-- ... -->
  
  <!-- 아래처럼 link 태그에도 적용될 수 있다. -->
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
  
  <!-- DTL 에서 제공하는 것 외에 것들을 가져오려면 -->
  <!-- load 를 사용한다. 여기에선 static 을 불러온다. -->
  {% load static %}
  <!-- static 폴더 내 articles 폴더를 만들어서 -->
  <!-- articles/sad.png 와 같이 설정할 수 있다. -->
  <img src="{% static 'sad.png' %}" alt="Error"></img>
  
  <!-- ... -->
  ```

  * DTL 에서 제공하는 것 외의 것들을  사용하려면 위와 같이 {% load 사용할 것 %} 형식을 취한다.



## django-bootstarp5 패키지

* 설치

  ```bash
  $ pip install django-bootstrap5
  ```

* INSTALLED_APPS 설정

  ```python
  # pjt/settings.py
  
  """
  ...
  """
  
  INSTALLED_APPS = [
      # ...
      # 언더바임을 유의하자!!
      'django_bootstrap5',
      # ...
  ]
  ```

* 사용

  ```html
  <!-- articles/create.html -->
  
  {% extends 'base.html' %}
  
  <!-- django-bootstrap 설정 -->
  <!-- 주의사항으로 아래 3줄은 반드시 block 안에 들어가야 한다. -->
  <!-- 아니면 base.html 에 추가하던가 -->
  <!-- 정확한 이유는 모르겠다. -->
  <!-- 하지만 block 과 관련이 있다는 것은 확실하다. -->
  <!-- {% block content %} -->
  {% load django_bootstrap5 %}
  {% bootstrap_css %}
  {% bootstrap_javascript %}
  
  <!-- 형식은 'bootstrap_태그이름 받을 데이터' 으로 사용한다. -->
  <!-- 또는 'bootstrap_태그이름 속성="값", ... ' 으로 사용한다. -->
  {% bootstrap_form article_form %}
  {% bootstrap_button button_type="submit" content="OK" %}
  <!-- ... -->
  
  <!-- {% endblock %} -->
  ```




## 참고자료

[1] [admin 페이지에서 등록한 Model 의 객체 조회할 때 제목 바꾸기 : ModelAdmin.list_display 부분](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/)

[2] [ModelAdmin.fields 에 대한 설명](https://docs.djangoproject.com/ko/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display)

[3] [django-bootstrap5 설정](https://pypi.org/project/django-bootstrap5/)