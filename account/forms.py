from django import forms
from django.core.exceptions import ValidationError

from account.models import User


class RegisterForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "full name", "class": "un"}), label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "email", "class": "un"}), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "password", "class": "un"}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "confirm password", "class": "un"}),
                                label='')

    def clean_password2(self):
        password = self.cleaned_data.get('password1')
        confirm_password = self.cleaned_data.get('password2')

        if password != confirm_password:
            raise ValidationError('password != confirm password')
        return confirm_password

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 8:
            raise ValidationError('password must more than 8 char and number !!!')
        return password1


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "email", "class": "un"}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "password", "class": "un"}), label='')


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "email", "class": "un"}), label='')


class ResetPasswordForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "new password", "class": "un"}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "confirm new password", "class": "un"}),label=''),
