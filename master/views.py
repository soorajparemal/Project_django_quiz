from django.shortcuts import render
from .models import main
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
# Create your views here

@csrf_exempt
def main_page(request):
    quiz=main.objects.all()
    context={'quiz':quiz}
    return render(request ,'master/mainpage.html',context)

score=0

def result_page(request):
    quiz=main.objects.all()
    global score

    for quizes in quiz:
        right=quizes.answer
        entered=request.POST.get(str(quizes.id))
        if(right==entered):
            score += 1
    context={'score':score}
    return render(request,'master/result.html',context)

def user_page(request):
    return render(request ,'master/userpage.html')

def teacher_page(request):
    quiz =main.objects.all()
    global score
    context={'score':score}
    return render(request, 'master/teacher.html',context)


def certificate_page(request):
    quiz = main.objects.all()
    context = {'score': score}
    return render(request, 'master/certificate.html', context)

def user(request):
    det=main.objects.all()
    users=User.objects.all()
    context = {'users':users,'det':det}
    return render(request,'master/user.html',context)

def answerpage(request):
    quiz=main.objects.all()
    context={'quiz':quiz}
    return render(request,'master/answer_page.html',context)