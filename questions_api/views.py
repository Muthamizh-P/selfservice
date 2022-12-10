from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import viewsets
from questions_api.models import *
from questions_api.serializers import QuestionsSerializer
from django.core.mail import send_mail


# Create your views here.
class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


def check_answer(request):
    count = 0
    if request.method == 'GET':
        print(request.GET)
        for key, value in request.GET.items():
            if Questions.objects.filter(question=key, answer=value):
                count += 1
            else:
                break
        print(count)
        if count < 5:
            return redirect("incorrect")
        else:
            return redirect("mail_screen")
    else:
        return redirect("forgot_username")


def send_username_mail(request):
    if request.method == 'POST':
        username = User.objects.get(email=request.POST['email']).username
        send_mail(
            'Your Username',
            'Your Username is - ' + username,
            'admin@selfservice.com',
            [request.POST['email']],
            fail_silently=False,
        )
        messages.success(request, 'Mail sent, Check your mail')
        return redirect('mail_screen')
