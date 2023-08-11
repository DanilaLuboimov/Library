from smtplib import SMTPSenderRefused

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from django.conf import settings

from .forms import RegisterForm, FeedbackForm


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/")

        form = RegisterForm()
        return render(request, "user/register.html", {"form": form})

    @transaction.atomic
    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/")

        return render(request, "user/register.html", {"form": form})


class AnotherLoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse(
                    data={
                        'status': 201
                    },
                    status=200
                )
            return JsonResponse(
                data={
                    'status': 400,
                    'error': 'Логин или пароль недействительны'
                },
                status=200
            )
        return JsonResponse(
            data={
                'status': 400,
                'error': 'Введите логин и пароль'
            },
            status=200
        )


class FeedbackView(View):
    @transaction.atomic
    def post(self, request):
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            email = request.POST.get('email')
            name = request.POST.get('first_name')

            if name:
                name = f", {name}"

            message = "Мы получили ваш запрос и скоро на него ответим."

            try:
                send_mail(
                    subject="Обратная связь",
                    message=None,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False,
                    html_message=f"Добрый день<b>{name}</b>!<br>{message}"
                )
            except SMTPSenderRefused:
                pass

            return JsonResponse(
                data={
                    "status": 201,
                    "message": "Ваш запрос в обработке",
                },
                status=200
            )

        return JsonResponse(
            data={
                'status': 400,
                'error': 'Заполните поля: "Почтовый адрес" и "Сообщение".'
                         ' А также докажите, что вы не робот!'
            },
            status=200
        )


class AnotherLogoutView(LogoutView):
    next_page = "/"

