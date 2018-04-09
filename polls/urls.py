# coding:utf-8


from django.urls import path
from . import views


# 给当前文件的url添加命名空间，这样就不会在有多个app的detail、index时发生冲突。
# 在index.html中使用{% url 'polls:detail' question.id %}
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
