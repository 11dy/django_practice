from django.shortcuts import render
#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    question_list = Question.objects.order_by('-create_date') # 질문목록 획득, order by는 조회 결과를 (역순으로 > -)정렬하는 함수.
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)
    #render : 파이썬 데이터를 템플릿에 적용하여 HTML로 반환. .html 파일을 템플릿 파일이라고 함

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # pk는 Question 모델의 기본키(Primary Key)에 해당하는 값을 의미한다.
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

