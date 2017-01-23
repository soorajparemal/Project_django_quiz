from django.db import models
# Create your models here.

class main(models.Model):
    question=models.CharField(max_length=200)
    def __str__(self):
        return  self.question
    pub=models.DateTimeField('Date Published')
    one=models.CharField(max_length=200)
    two=models.CharField(max_length=200)
    three=models.CharField(max_length=200)
    five=models.CharField(max_length=200)
    answer=models.CharField(max_length=200)

