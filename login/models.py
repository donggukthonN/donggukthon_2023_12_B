from django.db import models

class Member(models.Model):
    user_id = models.CharField(db_column='User_ID', primary_key=True, max_length=30)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30)  # Field name made lowercase.
    nickname = models.CharField(db_column='NickName', max_length=30)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase
    
    # class Meta로 mysql에 설정해둔 테이블 이름을 임의대로 불러와서 매핑시킬 수 있다
    # 이게 없었다면 login_member가 되어서 mysql에도 login_member 테이블이 있어야 한다
    class Meta:
        db_table = 'member' 