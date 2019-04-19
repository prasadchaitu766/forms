from django.db import models

class Feedback_Form(models.Model):
    f_name=models.CharField(max_length=30)
    l_name=models.CharField(max_length=20)
    email=models.EmailField()
    comment=models.TextField()
