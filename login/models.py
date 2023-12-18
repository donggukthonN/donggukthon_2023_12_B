from django.db import models

class Member(models.Model):
    user_id = models.CharField(db_column='User_ID', primary_key=True, max_length=30)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=30)  # Field name made lowercase.
    nickname = models.CharField(db_column='NickName', max_length=30)  # Field name made lowercase.
    code = models.IntegerField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase