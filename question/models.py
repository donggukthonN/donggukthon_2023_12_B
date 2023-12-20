from django.db import models
from login.models import Member

class Question(models.Model):
    num = models.IntegerField(db_column='Num', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=100, blank=True, null=True)  # Field name made lowercase.

    print(content)
    def get_content_with_newlines(self, line_length=15): # 여기서 line_length가 글자 수 몇 개마다 자를건지 정함
        # content를 일정 길이(line_length)마다 자르고 개행을 추가
        return '\n'.join([self.content[i:i+line_length] for i in range(0, len(self.content), line_length)])

    
    # for x in myresult:
    #     print("\n")
    # x = x[0]
    # new_str = ''
    # count = 0
    # for i, char in enumerate(x):
    #     if char == ' ':
    #         count += 1
    #     if count == 3:
    #         new_str += '\n'
    #         new_str += x[i+1:]  # 세 번째 띄어쓰기 이후의 모든 문자를 한 번에 추가합니다.
    #         break  # 더 이상의 탐색을 중지하고 다음 문장으로 넘어갑니다.
    #     else:
    #         new_str += char
    # print(new_str)
    
    
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