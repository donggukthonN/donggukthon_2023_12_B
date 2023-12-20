from django.db import models
from login.models import Member

class Question(models.Model):
    num = models.IntegerField(db_column='Num', primary_key=True)
    content = models.CharField(db_column='CONTENT', max_length=100, blank=True, null=True)
    
    def get_content_with_newlines(self):
        new_str = ''
        count = 0

        for char in self.content:
            new_str += char

            if char == ' ':
                count += 1

            if count == 3:
                new_str += '\n'
                count = 0  # 빈칸(공백) 개수가 3개일 때마다 count를 초기화하여 다음 묶음에 대한 체크를 시작합니다.

        return new_str
    
    def get_content_with_newlines2(self):
        new_str = ''
        count = 0

        for char in self.content:
            new_str += char

            if char == ' ':
                count += 1

            if count == 2:
                new_str += '\n'
                count = 0  # 빈칸(공백) 개수가 3개일 때마다 count를 초기화하여 다음 묶음에 대한 체크를 시작합니다.

        return new_str

    class Meta:
        managed = False
        db_table = 'question'
        

class Answer(models.Model):
    user = models.OneToOneField(Member, models.DO_NOTHING, db_column='User_ID', primary_key=True)  # Field name made lowercase. The composite primary key (User_ID, Num) found, that is not supported. The first column is selected.
    num = models.ForeignKey(Question, models.DO_NOTHING, db_column='Num')  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=350, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='FLAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'answer'
        unique_together = (('user', 'num'),)