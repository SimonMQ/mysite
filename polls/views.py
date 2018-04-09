from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse


# Create your views here.
# 首页显示最近发布的5个投票问题，以空格分割
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context=context)


# 问题详情页，先根据question的ID获取其实例对象，然后将其内容渲染到html
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
        }
    return render(request, 'polls/detail.html', context=context)


# 投票结果页，根据question的id返回相应对象
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/results.html', context=context)


# 投票页,先获取投票的对应question对象,然后获取用户选择的对应问题id
# 如果用户没选取直接提交,则重定向到本页,并返回一个错误提示信息
# 用户选好后提交,则对应投票项目加一,然后返回对象id的results页面
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
