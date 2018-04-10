# coding:utf-8

from django.contrib import admin
from .models import Question, Choice
# Register your models here.


# 用表格的方式来显示后台效果(tabular)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# 将后台表单分为及格字段集合
# fieldset元组中第一个元素是字段集的标题(可以为None)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('问题内容', {'fields': ['question_text']}),
        ('日期信息', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
