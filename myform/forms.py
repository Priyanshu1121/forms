from django import forms

class TextForm(forms.Form):
    question_text=forms.CharField(label='Question', max_length=250 )

class McqForm(forms.Form):
    question_text=forms.CharField(label='Question', max_length=250)
    option1=forms.CharField(label='option1', max_length=250)
    option2=forms.CharField(label='option2', max_length=250)
    option3=forms.CharField(label='option3', max_length=250)
    option4=forms.CharField(label='option4', max_length=250)

class BooleanForm(forms.Form):
    question_text=forms.CharField(label='Question', max_length=250)
    option=forms.CharField(label='Type',max_length=250)