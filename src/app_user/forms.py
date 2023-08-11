from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, \
    UsernameField
from django.utils.translation import gettext_lazy as _

from captcha.fields import ReCaptchaField

from .models import User, Feedback


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "class": "form-control",
            "style": "width: 300px"
        }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            "class": "form-control",
            "style": "width: 300px"
        }),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = (
            "username", "email", "password1", "password2",
            "last_name", "first_name", "phone_number",
        )
        widgets = {
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "style": "width: 300px"
            }),
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "style": "width: 300px"
            }),
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "style": "width: 300px"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "style": "width: 300px"
            }),
            "phone_number": forms.TextInput(attrs={
                "class": "form-control",
                "style": "width: 300px"
            }),
        }


class AuthForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "class": "form-control",
            }
        ),
        label="Логин"
    )
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": "form-control",
            }
        ),
    )


class FeedbackForm(forms.ModelForm):
    captcha_v3 = ReCaptchaField(label="")

    class Meta:
        model = Feedback
        fields = (
            "email", "first_name", "message", "phone_number", "captcha_v3"
        )
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
        }
