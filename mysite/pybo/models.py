from django.db import models

# Create your models here.
from django.db import models

# 질문 모델에 필요한 속성들. 질문 제목, 내용, 작성한 일시
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject # id 값 대신 제목 표시

# 질문, 답변의 내용, 답변 작성 일시
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)# 답변과 연결된 질문이 삭제될 경우 답변도 함께 삭제된다.
    content = models.TextField()
    create_date = models.DateTimeField()
# 기존 모델을 속성으로 연결하려면 Foreignkey를 사용해야 한다. Foreignkey는 다른 모델과 연결하기 위해
#사용한다.