from django.db import models
from login.models import Member

class Question(models.Model):
    num = models.IntegerField(db_column='Num', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'question'


class Answer(models.Model):
    user = models.OneToOneField(Member, models.DO_NOTHING, db_column='User_ID', primary_key=True)  # Field name made lowercase. The composite primary key (User_ID, Num) found, that is not supported. The first column is selected.
    num = models.ForeignKey(Question, models.DO_NOTHING, db_column='Num')  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=350)  # Field name made lowercase.
    flag = models.IntegerField(db_column='FLAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'answer'
        unique_together = (('user', 'num'),)