# django-05

* DTL(Django Template Language) 에서 제공하는 문법으로 url 을 지정하는 방법을 배웠다.
* URL 이름이 같을 경우를 해결하기 위한 방법인 URL NameSpace 을 배웠다.
* 장고의 패턴은 MVC 패턴을 기반으로 한 MTV 패턴이다. 
* django render, redirect 함수의 차이
* DTL 에서 제공하는 URL 문법으로 데이터도 같이 넘기기를 배웠다.



## DTL에서 제공하는 문법으로 URL 을 지정하는 방법

* URL 값을 넣을 때는 ```"{% url '해당 URL 이름'%}"``` 형식을 사용하여 지정한다.

* views.py 에서 URL 이름 지정 방법

  ```python
  #views.py
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('', views.index, name='index'),
  ]
  ```

  * 위와 같이 keyword argument 중 name 을 지정하여 사용할 수 있다.

* 하드코딩된 URL 값이 아닌 변수를 활용할 수 있다는 점에서 유지보수 측면에서 이점을 가져올 수 있다.

* 그런데 만약 여러 앱에서 URL 명을 같은 것으로 지정하게 되면 어느 것을 택할지 알 수가 없다.

* 따라서 이것을 해결할 수 있는게 **URL NameSpace** 이다.

  

## URL NameSpace

* 매우 단순하다. 각 앱의 ```views.py``` 에 ```app_name``` 이라는 변수에다가 앱 이름을 할당하면 된다.

  ```python
  # app1/views.py
  from django.urls import path
  from . import views
  
  app_name = 'app1'
  
  urlpatterns = [
      path('', views.index, name='index'),
  ]
  ```

* 그런 다음 html 파일에서는 다음과 같이 ```{% url '앱이름:별칭' %}```으로 바꾸면 정상적으로 동작하게 된다.

  ```html
  <form action="{% url 'app1:index' %}">
      ...
  </form>
  ```

* 주의사항으로, ```app_name``` 을 지정한 이후에는 url 태그에서 반드시 ```앱이름:별칭``` 형태로만 사용해야 한다.

* 안그러면 NoReverseMatch에러가 뜬다.



## 장고의 패턴은 MTV이다.


* 장고는 MVC 패턴을 기반으로 두며 역할은 같으나 이름만 다른 패턴을 사용하는 셈이다.
|    MVC     |   MTV    |
| :--------: | :------: |
|   Model    |  Model   |
|    View    | Template |
| Controller |   View   |

* Model
  * 데이터 관련 로직 관리를 한다.
  * 응용 프로그램 데이터 구조 정의와 DB 기록 관리를 한다.
* Template
  * 레이아웃, 화면 처리를 한다.
  * 화면 상 UI 구조 및 레이아웃 정의를 한다.
* View
  * Model 과 Template 관련 로직 처리하여 응답을 반환한다.
  * 클라이언트 요청에 대한 처리를 분기하는 역할을 담당한다.



## django render, redirect 함수의 차이

* render(***request***, **template_name**, **context=None**, **content_type=None**, **status=None**, **using=None**)
  * 리턴값으로 인자로 지정된 template 과 context 딕셔너리를 합쳐서 HttpResponse 객체를 반환한다.
  * 여기서 지정된 template 에 딕셔너리 형태로 데이터를 넘겨줄 수 있는 부분이 context 부분이다.
  
* redirect(**to**, ***args**, **permanent=False**, ** **kwargs**)
  * 넘어온 arguments 에 대하여, 적절한 URL 에 HttpResponseRedirect 객체를 반환한다.
  
  * 특정 URL 을 넘기면 해당 URL 로 넘어간다. 
  
  * URL 로 이동하는 것이기 때문에 argument 에 데이터를 넣어서 넘길 수 있다.
  
    ```python
    """
    ...
    """
    
    post = Post.objects.get(pk=_pk)
    
    return redirect('posts:detail', post.pk)
    ```
  
  * url path 를 직접 적거나 혹은 urlpattern 에서 지정한 name 값을 지정할 수있다. 



## DTL 에서 제공하는 URL 문법으로 데이터도 같이 넘기기

* 동적인자로써 넘기는 방법이 있다.

* html 파일은 DTL 에서 제공하는 URL 문법에 넘어온 데이터를 활용하는 방법을 사용한다.

* 그리고 각 앱에 존재하는 ```urls.py```  파일에 해당 URL 의 **동적인자** 표기를 반드시 사용 해야한다.

  ```html
  <!-- html 파일 -->
  
  <a href="{% url '앱이름:url' 데이터.속성 %}"></a>
  ```

  ```python
  # 앱이름/urls.py
  """
  ...
  """
  
  app_name = '앱이름'
  
  urlpatterns = [
      # 반드시 동적인자 url 에 명시해야 한다.
      path('url/<자료형:속성>', views.함수)
  ]
  ```
  
  



## 참고자료

[1] [render, redirect함수](https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#django.shortcuts.render)

[2] [render, redirect 함수 차이](https://velog.io/@rosewwross/Django-render-%EC%99%80-redirect%EC%9D%98-%EC%B0%A8%EC%9D%B4)