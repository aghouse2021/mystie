from django.db import models

import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published',default=timezone.now)

    def __str__(self):
        return f'{self.question_text}'

    def was_published_recently(self):
        current_date = timezone.now()
        recent_date_with_offset = current_date - datetime.timedelta(days=1)
        return   recent_date_with_offset <= self.pub_date <= current_date

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.choice_text}({self.votes})"


