from django.db import models
from login.models import Member

class Friend(models.Model):
    user = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)
    f_id = models.CharField(max_length=30, blank=True, null=True)    

    class Meta:
        managed = False
        db_table = 'friend'