from django.db import models
import pytz
import jdatetime
from django.utils import timezone

# Create your models here.

class Log(models.Model):
    ip = models.CharField(max_length=30)
    host = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    to = models.CharField(max_length=100)
    subject = models.CharField(max_length=1000)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip

    class Meta:
        db_table = "Log"

    def jalali_datetime(self):
        tz = pytz.timezone('Asia/Tehran')
        dt = self.datetime.astimezone(tz)
        j_date = jdatetime.datetime.fromgregorian(datetime=dt)
        return j_date.strftime('%d-%m-%Y  |  %H:%M')