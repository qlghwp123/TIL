from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # 반드시 리스트 또는 튜플이어야 한다.
    fields = ['title', 'content']
    # 조회 시 해당 필드의 값으로 제목 변경
    list_display = ['title', 'content']

# 등록
admin.site.register(Article, ArticleAdmin)