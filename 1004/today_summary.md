# django - 07

* forms 클래스를 활용하여 자동으로 html 태그 생성을 배웠다.
* 서버쪽에서 입력 값에 대한 유효성 검사를 배웠다.
* forms 클래스, as_p field 사용할 때 페이지 update 부분을 배웠다.



## forms 클래스를 활용하여 자동으로 html 생성

* 예시 데이터 모델 클래스는 다음과 같다.

  ```python
  # models.py
  
  class Article(models.Model):
      title = models.CharField(max_length=20)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

* 유효성 검사를 위해 다음과 같이 파일을 생성하여 장고에서 제공하는 패키지를 사용한다.

* Meta 내부 클래스 내 field 속성 값을 특정 필드만으로 지정할 수 있다.

  ```python
  # forms.py : 파일 명은 자유롭게 작성해도 되지만 주로 이 이름을 많이 쓴다.
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.Modelform):
      
      # 아래 의미는 Article 의 모든('__all__') 필드를 가져다 쓴다는 의미이다.
      class Meta:
          # model 속성에는 사용할 모델 이름을 넣는다.
          model = Article
          field = '__all__'
          # 모든 필드가 아닌 특정 필드만 지정하고 싶을 때, 아래와 같이 사용할 수 있다.
          # field = ['title', 'content']
  ```

* 그럼 위 클래스를 활용하여 기존 views.py 와 html 파일도 아래와 같이 바뀔 수 있다.[1] [2]

  ```python
  # views.py
  """
  ...
  """
  from .forms import ArticleForm
  
  """
  ...
  """
  
  def new(request):
      article_form = ArticleForm
      
      return render(request, 'articles/new.html', {'article_form': article_form})
  ```

  ```html
  <!-- new.html -->
  <h1>
      글쓰기
  </h1>
  
  <form action="{% url 'articles:create' %}" method="POST">
      {% csrf_token %}
      <!-- 아래는 추가한 코드, 렌더링 결과는 같다. -->
      {{ article_form.as_p }}
      
      <!-- 아래는 원본 -->
      <!-- <label for="title">제목 : </label> -->
      <!-- <input type="text" name="title" id="title" required> -->
      <!-- <label for="content">내용 : </label> -->
      <!-- <textarea name="content" id="content" cols="30" rows="10" required></textarea> -->
      <!-- <input type="submit" value="글쓰기"> -->
  </form>
  ```

* 그럼 이거 왜 쓸까?

  * field 가 10개만 넘어도 일일이 수작업으로 작성하기에는 같은 코드의 반복 및 유지보수가 힘들다.
  * 하지만 위와 같은 forms 클래스를 활용하면 아주 쉽고 간결하게 코드를 작성할 수 있다.

* 그러면 CSS는 어떻게 적용하나?

  * ~~그것은 따로 찾아봐야 한다. 공식문서를 추후에 뒤져서 기록할 예정이다!~~
  * 이것은 [2] 의 **폼 위젯**을 살펴보면 된다!



## 서버쪽에서 입력 값에 대한 유효성 검사

* 예시로 글을 쓰는 기능이 있다고 가정한다.

  ```python
  # views.py
  """
  ...
  """
  from .forms import ArticleForm
  
  """
  ...
  """
  
  def create(request):
      if request.method == 'POST':
          article_form = ArticleForm(request.POST)
  
          # 실질적으로 유효성 검사를 하는 메소드이다.
          if article_form.is_valid():
              article_form.save()
              return redirect('articles:index')
      else:
          article_form = ArticleForm()
      
      # invalid 일 때를 생각해야 하므로 else 블록 안에 들어가면 안된다.
      return render(request, 'articles/new.html', {'article_form': article_form})
  ```

  ```html
  <!-- new.html -->
  <h1>
      글쓰기
  </h1>
  
  <form action="{% url 'articles:create' %}" method="POST">
      {% csrf_token %}
      <!-- 아래는 추가한 코드, 렌더링 결과는 같다. -->
      {{ article_form.as_p }}
      
      <!-- 아래는 원본 -->
      <!-- <label for="title">제목 : </label> -->
      <!-- <input type="text" name="title" id="title" required> -->
      <!-- <label for="content">내용 : </label> -->
      <!-- <textarea name="content" id="content" cols="30" rows="10" required></textarea> -->
      <!-- <input type="submit" value="글쓰기"> -->
  </form>
  ```

  * 해당 html 에서 입력을 넣을 때, 한 개라도 입력하지 않으면 DB 에 저장은 되지 않는다.
  * 왜냐하면 is_valid() 메소드를 통해서 유효성 검사가 진행된다.[3]

  

## forms 클래스, as_p field 사용할 때 페이지 update 부분

* update.html

  ```html
  <!-- update.html -->
  <h1>글 수정하기</h1>
  
  <form action="" method="POST">
      {% csrf_token %}
      {{ article_form.as_p }}
      <input type="submit" value="수정">
  </form>
  ```

  * 여기서 action 이 비어있는데 이것은 일종의 트릭으로, 비워두면 현재 페이지 URL 이 default 로 설정된다.
  * 어차피 url은 /articles/update 로  같지만 GET, POST 동작만 다르게 하기 때문에 현재 페이지를 나타내는 이다.
  * 따라서 같은 템플릿을 여러 번 사용할 때 이런 트릭이 사용된다.

* view.py

  ```python
  """
  ...
  """
  
  def update(request, pk):
      # URL로 넘어온 id 값을 통해서 DB 에 저장되어 있는 데이터를 가져온다.
  	article = Article.objects.get(pk=pk)
      
      if request.method == 'POST':
          # forms subclass 인 ArticleForm 클래스의 생성자를 초기화할 때,
          # keyword argument 중 instance 를 활용해서 특정 모델을 지정할 수 있다.
          # 이렇게 되면 수정 페이지가 렌더링될 때, 기존 데이터들이 입력 값으로 설정되어
          # 화면에 보이게 된다.
      	article_form = ArticleForm(request.POST, instance=article)
          
          if article_form.is_valid():
              return redirect('articles:detail', article.pk)
      else:
          # 특이하게 POST 와는 달리 GET 의 경우 request 관련 인자를 사용하지 않는다.
          article_form = ArticleForm(instance=article)
          
      return render(request, 'articles/update.html', {'articles': article_form})
  ```

  * 눈여겨 볼 부분은 ArticleForm 객체를 생성하는 부분이다.

  * ArticleForm class 는 ModelForm 의 subclass 이다. 

  * ArticleForm 클래스의 생성자를 초기화 부분을 보면 keyword argument 중 instance 를 활용해서 특정 모델을 지정할 수 있다.[4]

  * 이 때, GET POST 가리지 않고 초기화에 반드시 instance keyword argument 를 지정한다.

  * 생각해보면 Model, ModelForm 은 다른 클래스이긴 하니까 기존 데이터가 Model 클래스이므로 따로 지정을 해줘야 함을 다시 생각해보면 알 수 있긴하다.
  
    

## 참고자료

[1] [as_p 공식문서](https://docs.djangoproject.com/en/3.2/ref/forms/api/)

[2] [as_p 위키닥스](https://wikidocs.net/70855)

[3] [is_valid 메소드](https://docs.djangoproject.com/en/3.2/ref/forms/api/#django.forms.Form.is_valid)

[4] [ModelForm 생성자 (The save() method 부분)](https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/)

