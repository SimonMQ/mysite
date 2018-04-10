# coding:utf-8


from django.urls import path
from . import views


# 给当前文件的url添加命名空间，这样就不会在有多个app的detail、index时发生冲突。
# 在index.html中使用{% url 'polls:detail' question.id %}
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
