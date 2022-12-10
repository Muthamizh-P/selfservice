import json
import random

import requests
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect
from questions_api.models import *

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import *
from django.contrib.auth.decorators import login_required


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def forgot_username(request):
    scheme = request.scheme + '://'
    questions = requests.get(scheme + request.get_host() + '/questions/question/').json()
    if len(questions) > 5:
        random_questions = random.sample(questions, 5)
    else:
        random_questions = random.sample(questions, len(questions))
    context = {
        "questions": random_questions
    }
    return render(request, 'accounts/forgot_username.html', context)


def login_index(request):
    return render(request, 'registration/login_index.html')


def mail_screen(request):
    return render(request, 'accounts/mail_screen.html')


def password(request):
    return render(request, 'registration/login.html')


def incorrect(request):
    return render(request, 'accounts/incorrect.html')


def check_mail_exist(request):
    username = request.POST['username']
    if request.method == 'POST':
        if User.objects.filter(username=username).exists():
            return redirect("login")
        else:
            messages.error(request, 'Username is wrong')
            return redirect('login_index')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
