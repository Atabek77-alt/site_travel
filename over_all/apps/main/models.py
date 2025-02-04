from django.db import models
from django.contrib.auth.models import  BaseUserManager
# Create your models here.




class Appeal(models.Model):

    name = models.CharField('ФИО', max_length=100)
    email = models.EmailField('Почта', unique=True)
    subject = models.CharField('Тема',max_length=60, blank=True,null=True)
    message = models.TextField('Сообщение',null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'



    def __str__(self):
        return self.name
