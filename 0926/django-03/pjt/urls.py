"""pjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
