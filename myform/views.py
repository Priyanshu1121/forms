from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
#from . import forms
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
"""
def createformview(request):
    from django.http import HttpResponseRedirect
from django.shortcuts import render
"""
#@login_required
def register(request):
    context={}
    form=UserCreationForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            user =form.save()
            login(request,user)
            return render(request,'myform/formlist.html')
    context['form']=form
    return render(request,'registration/register.html',context)

"""def loginview(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return render(request,'myform/formlist.html',user)
    return render(request,'registration/login.html')"""


def createtextformview(request,form):
    username=request.user.username
    user=User.objects.get(username=username)
    questions=TextForm.objects.filter(form_id=form,user_id=user)
    questionsmcq=McqForm.objects.filter(form_id=form, user_id=user)
    questionsbool=BoolForm.objects.filter(form_id=form, user_id=user)
    form=Form.objects.get(form_id=form)
    server="127.0.0.1:8000"
    if (request.method == "POST") and (request.POST.get('type')=='text'):
        question_text = request.POST.get('question_text')
        #form=Form.objects.get(form_id=form)
        TextForm.objects.create(question_text=question_text,form_id=form, user_id=user)
        questions=TextForm.objects.filter(form_id=form, user_id=user)
        
        return render(request,'myform/form.html', {'questions':questions,'questionsmcq': questionsmcq,'questionsbool':questionsbool,'form':form,'server':server})
   
    
    if request.method == "POST" and (request.POST.get('type')=='mcq'):
        if request.POST.get('question_text'):
            question_text = request.POST.get('question_text')
            option1 = request.POST['option1']
            option2 = request.POST['option2']
            option3 = request.POST['option3']
            option4 = request.POST['option4']
            #form=Form.objects.get(form_id=form)
            McqForm.objects.create(question_text=question_text, user_id=user,form_id=form,option1=option1,option2=option2,option3=option3,option4=option4)
            questionsmcq=McqForm.objects.filter(form_id=form, user_id=user)
            print(request)
            return render(request,'myform/form.html', {'questions':questions,'questionsmcq': questionsmcq,'questionsbool':questionsbool,'form':form,'server':server})

    
    if request.method == "POST" and (request.POST.get('type')=='bool'):
        if request.POST.get('question_text'):
            question_text = request.POST.get('question_text')
            
            #form=Form.objects.get(form_id=form)
            BoolForm.objects.create(question_text=question_text,form_id=form ,user_id=user)
            questionsbool=BoolForm.objects.filter(form_id=form, user_id=user)
            print(request)
            return render(request,'myform/form.html', {'questions':questions,'questionsmcq': questionsmcq,'questionsbool':questionsbool,'form':form,'server':server})
    else:
        print(request)
        return render(request, "myform/form.html", {'questions':questions,'questionsmcq': questionsmcq,'questionsbool':questionsbool,'form':form,'server':server})
@login_required(login_url='/login')
def formview(request, form): 
    username=request.user.username
    user=User.objects.get(username=username)
    form=Form.objects.get(form_id=form)
    questions=TextForm.objects.filter(form_id=form)
    questionsmcq=McqForm.objects.filter(form_id=form) 
    questionsbool=BoolForm.objects.filter(form_id=form)   
    if request.method == "POST" :
        
        i=1
        for question in questions:
            if request.POST.get('question'+str(i)):
                answer_text= request.POST.get('question'+str(i))
                TextAnswer.objects.create(answer_text=answer_text,form_id=form,question_id=question, user_id=user)
                print(request.POST.get('question'+str(i)),request)
            else:
                print(request.POST.get('question'+str(i)),request)
            i+=1
        j=1
        for question in questionsmcq:
            if request.POST.get('questionmcq'+str(j)):
                answer_text= request.POST.get('questionmcq'+str(j))
                McqAnswer.objects.create(answer_text=answer_text,form_id=form,question_id=question,user_id=user)

            else:
                print(request.POST.get('questionmcq'+str(j)),request)
            j+=1
        
        k=1
        for question in questionsbool:
            if request.POST.get('questionbool'+str(k)):
                answer_text= request.POST.get('questionbool'+str(k))
                BoolAnswer.objects.create(answer_text=answer_text,form_id=form,question_id=question,user_id=user)

            else:
                print(request.POST.get('questionbool'+str(k)),request)
            k+=1
        return render(request,'myform/open.html',{'questions':questions,'questionsmcq':questionsmcq,'questionsbool':questionsbool,'form':form})
    else:
        return render(request, "myform/open.html",{'questions':questions,'questionsmcq':questionsmcq,'questionsbool':questionsbool,'form':form})


def answersview(request,form):
    answers=TextAnswer.objects.filter(form_id=form)
    answersmcq=McqAnswer.objects.filter(form_id=form)
    answersbool=BoolAnswer.objects.filter(form_id=form)
    form=Form.objects.get(form_id=form)
    u=[]
    for a in answers:
        if a.user_id not in u:
            u.append(a.user_id)
    for a in answersmcq:
        if a.user_id not in u:
            u.append(a.user_id)
    for a in answersbool:
        if a.user_id not in u:
            u.append(a.user_id)
    
    if request.POST.get('u'):
        u=request.POST.get('u')
        u=User.objects.get(username=u)
        answers=TextAnswer.objects.filter(form_id=form,user_id=u)
        answersmcq=McqAnswer.objects.filter(form_id=form,user_id=u)
        answersbool=BoolAnswer.objects.filter(form_id=form,user_id=u)

    
    return render(request,'myform/answer.html',{'answers':answers,'answersmcq':answersmcq,'answersbool':answersbool,'u':u,'form':form})


def createformview(request):
    username=request.user.username #data.get('username')
    user=User.objects.get(username=username)
    forms=Form.objects.filter(user_id=user)
    if request.method=="POST":
        if request.POST['form_name']:
            form_name=request.POST['form_name']
            Form.objects.create(name=form_name, user_id=user)
        else:
            print(request.POST['form_name'])
    return render(request,'myform/formlist.html',{'forms':forms})
    
"""def create(request):
    if request.method=="POST":
        if request.POST['question_text']:
            x=request.POST['question_text']
            tex=TextForm()
            tex.question_text=x
            tex.save()
            return render(request,"myform/form.html")
        return render(request,'myform/open.html')"""

def testsubmit(request):   
    if request.method == "POST":
        data = request.POST['fdata']
        TestInput.objects.create(data=data)
        return HttpResponse("<!DOCTYPE html><html><body><h1>Response submitted!</h1></body></html>")
    else:
        return render(request, "myform/formx.html")