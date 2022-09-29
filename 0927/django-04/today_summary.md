# django-04

* 배운 것들은 3개이다.
* 프로젝트 내 urls.py 내 url들을 분리하여 각 앱들이 해당하는 url 들을 관리하게 만든다.
* django 가 templates 폴더를 읽을 때, 이름이 중복되면 안된다.
* form 태그에서 action 속성 값으로 특정 url 로 설정할 경우 주의가 필요하다.



## 앱 별로 url 들을 관리(App URL mapping)

* django 프로젝트 폴더 내 urls.py 파일에 여러 앱 url 들이 몰려있을 때

* 아래와 같이 앱이 많아질 수록 많아지고 유지보수가 어려워진다. 

  ```python
  #pjt/urls.py
  
  from django.contrib import admin
  from django.urls import path
  from calculate.views import calculate
  from isOddEven.views import is_odd_even
  from pastLife.views import past_life_input
  from lorem.views import lorem_input, lorem_result
  from pastLife.views import past_life
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('calculate/<first>/<second>/', calculate),
      path('is-odd-even/<val>/', is_odd_even),
      path('past-life-input/', past_life_input),
      path('lorem-input/', lorem_input),
      path('lorem-result/', lorem_result),
      path('past-life-result/', past_life),
  ]
  ```

* 따라서 앱 별로 url 들을 분리시켜서 각 앱에서 관리하는 방법이 있다.

* 아래는 적용 후이다.
  ```python
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('calculate/', include('calculate.urls')),
      path('is-odd-even/', include('isOddEven.urls')),
      path('past-life/', include('pastLife.urls')),
      path('lorem/', include('lorem.urls')),
  ]
  
  ```

  ```python
  # caculate/urls.py
  from django.urls import path
  from . import views
  
  app_name = calculate
  
  urlpatterns = [
      path('<first>/<second>/', views.calculate),
  ]
  ```

  ```python
  # is_odd_even/urls.py
  from django.urls import path
  from . import views
  
  app_name = is_odd_even
  
  urlpatterns = [
      path('<val>/', views.is_odd_even),
  ]
  ```

  ```python
  # pastLife/urls.py
  from django.urls import path
  from . import views
  
  app_name = pastLife
  
  urlpatterns = [
      path('input/', views.past_life_input),
      path('result/', views.past_life),
  ]
  ```

  ```python
  # lorem/urls.py
  from django.urls import path
  from . import views
  
  app_name = lorem
  
  urlpatterns = [
      path('input/', views.lorem_input),
      path('result/', views.lorem_result),
  ]
  ```


* 이 때 주의 사항으로 반드시 각 앱의 urls.py 내 **urlpatterns** 변수가 없으면 에러를 일으킨다.
  
  

## django 가 templates 폴더를 읽을 때

* django 에서 여러 앱이 있을 때, 각 앱의 templates 폴더를 읽는다.

* 이 때, 아래와 같이 이름이 중복될 경우 올바르게 작동하지 않는다. 

  ```
  app1
  	templates
  		index.html
  app2
  	templates
  		index.html
  ```

* 따라서 아래와 같이 app_name/templates/app_name/file.html 형식을 유지해야 한다.

* views.py 에는 html 파일을 지정할 때 'app_name/file.html' 형식으로 바꿔줘야 한다. 

  ```
  app1
  	templates
  		app1
  			index.html
  app2
  	templates
  		app2
  			index.html
  ```

  ```python
  # view.py
  
  """
  ...
  """
  
  return render(req, "app_name/file.html")
  ```



## form 태그에서 action 속성 값으로 특정 url 로 설정할 경우

* 특정 url 로 넘길 때 기존 url 에서 더해지는 경우 : 반드시 첫 번째 글자로 / 가 와야한다.

* 다음과 같은 태그가 있고 기존 페이지 URL 이 ```localhost:8080/todo/```  인 경우가 있다고 하자.

  ```html
  <form action="todo/create/" method="GET">
    ...  
  </form>
  ```

* 최종 URL 은 ```localhost:8080/todo/todo/create/``` 이다. 따라서 다음과 같이 변경해야 한다.

  ```html
  <form action="/todo/create/" method="GET">
    ...  
  </form>
  ```

* 어찌보면 당연한게 만약 ```/```가 없다면 현재 URL 기준으로 더해지는 의미이므로 저렇게 동작하는게 맞다.

* ```/```를 추가하면 브라우저, 장고 중 어떤 녀석인지는 몰라도 알아서 todo 의 create URL 로 지정해준다.
