from django.db import models

# Create your models here.
class Questions(models.Model):
    q_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    owner = models.ForeignKey('auth.User', related_name='Questions', on_delete=models.CASCADE)


class Choices(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.User', related_name='Choices', on_delete=models.CASCADE)