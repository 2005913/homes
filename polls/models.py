import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date>=timezone.now()- datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date' # 정렬 기준 항목
    was_published_recently.boolean = True #값이 boolean형태인지 설정하고 true이면 값대신 아이콘
    was_published_recently.short_description = 'Published recently' #헤더 이름


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text