from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Form(models.Model):
    form_id=models.AutoField( primary_key='True')
    name=models.CharField(max_length=150)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TextForm(models.Model):
    question_id=models.AutoField(primary_key="True")
    question_text=models.CharField(max_length=250)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    form_id=models.ForeignKey(Form, on_delete=models.CASCADE)
    def __str__(self):
        return self.question_text

class McqForm(models.Model):
    question_id=models.AutoField(primary_key="True")
    question_text=models.CharField(max_length=250)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    form_id=models.ForeignKey(Form, on_delete=models.CASCADE)
    option1=models.CharField(max_length=250)
    option2=models.CharField(max_length=250)
    option3=models.CharField(max_length=250)
    option4=models.CharField(max_length=250)
    def __str__(self):
        return self.question_text

class BoolForm(models.Model):
    question_id=models.AutoField(primary_key="True")
    question_text=models.CharField(max_length=250)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    form_id=models.ForeignKey(Form, on_delete=models.CASCADE)
    #option=models.CharField(max_length=250)
    def __str__(self):
        return self.question_text


class TextAnswer(models.Model):
    answer_id=models.AutoField(primary_key='True')
    question_id=models.ForeignKey(TextForm,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    form_id=models.ForeignKey(Form,on_delete=models.CASCADE)
    answer_text=models.CharField(max_length=250 )

class McqAnswer(models.Model):
    answer_id=models.AutoField(primary_key='True')
    question_id=models.ForeignKey(McqForm,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    form_id=models.ForeignKey(Form,on_delete=models.CASCADE)
    answer_text=models.CharField(max_length=250)

class BoolAnswer(models.Model):
    answer_id=models.AutoField(primary_key='True')
    question_id=models.ForeignKey(BoolForm,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    form_id=models.ForeignKey(Form,on_delete=models.CASCADE)
    answer_text=models.CharField(max_length=250)

class TestInput(models.Model):
    data = models.CharField(max_length=50)