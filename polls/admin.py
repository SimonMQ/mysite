from django.contrib import admin
from .models import Question, Choice
# Register your models here.


# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ['question_text', 'pub_date']


admin.site.register(Question)
admin.site.register(Choice)
