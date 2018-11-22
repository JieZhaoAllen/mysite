from django.db import models
from datetime import datetime
import time
# Create your models here.


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= time.timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    """
    使用了 ForeignKey 定义了一个关联。它告诉 Django 每一个Choice 关联一个 Poll 。
     Django 支持常见数据库的所有关联：多对一（ many-to-ones ），多对多（ many-to-manys ） 和 一对一 （ one-to-ones ）。
    """
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text