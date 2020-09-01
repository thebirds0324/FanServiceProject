from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
import datetime

class OfficialPost(models.Model):
    title=models.CharField(max_length=50)
    imp=models.ImageField(upload_to='images')
    post=models.CharField(max_length=140)
    pub_date=models.DateTimeField('date published')
    #DataField('Career_Date')
    #IntegerField(default=0)
    #ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class NormalPost(models.Model):
    title = models.CharField(max_length=50)
    imp = models.ImageField(upload_to='images')
    post = models.CharField(max_length=140)
    pub_date = models.DateTimeField('date published')

    # DataField('Career_Date')
    # IntegerField(default=0)
    # ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Member(models.Model):
    nickname=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    id_receive=models.CharField(max_length=14)
    password_receive=models.CharField(max_length=20)

    def __str__(self):
        return self.nickname

    def __str__(self):
        return self.email

    def __str__(self):
        return self.id_receive

    def __str__(self):
        return self.password_receive