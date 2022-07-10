from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from .forms import QuestionForm, AnswerForm

def index(request):
    question_list = Question.objects.order_by('-create_date') # 질문목록 획득, order by는 조회 결과를 (역순으로 > -)정렬하는 함수.
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)
    #render : 파이썬 데이터를 템플릿에 적용하여 HTML로 반환. .html 파일을 템플릿 파일이라고 함

def detail(request, question_id): # pybo 내용 출력
    question = get_object_or_404(Question, pk=question_id) # pk는 Question 모델의 기본키(Primary Key)에 해당하는 값을 의미한다.
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

## 답변등록
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    form = QuestionForm()
    return render(request, 'pybo/question_form.html', {'form': form}) # 템플릿에서 질문 등록시 사용할 폼 엘리먼트를 생성

## 질문등록
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid(): # 폼이 유효한 경우
            question = form.save(commit=False) # 임시 저장(커밋=폴스)하여 QUESTION 객체를 리턴받는다.
            question.create_date = timezone.now() # 실제 저장을 위해 작성일시 설정
            question.save() # 데이터를 실제로 저장
            return redirect('pybo:index')
    else: #GET 방식일 경우 URL을 전달받아 질문 등록 화면 렌더링
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)