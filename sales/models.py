from django.db import models
from django.contrib.auth.models import AbstractUser


class 아이디(AbstractUser):
    pass

# Create your models here.
class Sale(models.Model):

    # 경로_선택 =(
    #     ('nr','네이버'),
    #     ('shop2','샵투월드')
    #     ('news','이메일뉴스레터')
    # )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)

    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"


    # 기존고객 = models.BooleanField(default=False)
    # 유입경로 = models.CharField(choices=경로_선택, max_length=200)
    # 인물사진 = models.ImageField(blank=True, null=True)
    # 파일 = models.FileField(blank=True, null=True)

    # python manage.py migrate 명령창에서 해야함

class Person(models.Model):
    회원 = models.OneToOneField(아이디, on_delete=models.CASCADE)

    def __str__(self):
        return self.회원.email

    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)