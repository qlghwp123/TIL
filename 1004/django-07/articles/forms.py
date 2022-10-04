from django import forms
from django import forms
from .models import Article

# 특정 모델에 대한 Form 클래스
class ArticleForm(forms.ModelForm):

    # 특정 모델과 해당 모델의 필드를 지정
    class Meta():
        model = Article
        fields = '__all__'
        # 특정 필드를 지정 시 다음과 같다.
        # fields = ['title', 'content']