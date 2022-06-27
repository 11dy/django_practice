from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin) #admin.site.register로 Question 모델을 등록했다
