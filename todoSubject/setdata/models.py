from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date=models.DateTimeField()

    #  id 값 대신 제목을 표시
    def __str__(self):
        return self.subject

# on_delete=models.CASCADE의 의미는 이 답변과 연결된 질문(Question)이 삭제될 경우 답변(Answer)도 함께 삭제
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date= models.DateTimeField()


