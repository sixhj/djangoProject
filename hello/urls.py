from django.urls import path

from hello.views import *

urlpatterns = [
    path('', HelloView.as_view()),
    path('world',world),
    path('question',index,name='question'), # name 对应的是html 名称
]
