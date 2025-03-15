from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.views import View
from account.forms import RegisterForm, LoginForm, ForgetPasswordForm, ResetPasswordForm
from account.models import User
from utils.email_service import send_email



class RegisterView(View):
    form_class = RegisterForm
    template_name = 'account/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home-page')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        register_form = self.form_class
        return render(request, self.template_name, {'register_form': register_form})

    def post(self, request):
        register_form = self.form_class(request.POST)
        if register_form.is_valid():
            cd = register_form.cleaned_data
            full_name = cd.get('full_name')
            email = cd.get('email')
            password = cd.get('password1')
            user = User.objects.filter(email__iexact=email).exists()

            if user:
                RegisterForm.add_error('email', 'There is email entered !!!')
            else:
                new_user = User(full_name=full_name, email_active_code=get_random_string(72), email=email,
                                is_active=True, username=email)
                new_user.set_password(password)
                new_user.email_active_code = get_random_string(72)
                new_user.save()
                return redirect('home:home-page')

        return render(request, self.template_name, {'register_form': register_form})


class LoginView(View):
    form_class = LoginForm
    template_name = 'account/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home-page')
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        login_form = self.form_class()
        return render(request, self.template_name, {'login_form': login_form})

    def post(self, request):
        login_form = self.form_class(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user:
                is_password_currect = user.check_password(user_password)
                if is_password_currect:
                    login(request, user)
                    return redirect('home:home-page')
                else:
                    login_form.add_error('password', 'password is wrong!')

            else:
                login_form.add_error('email', 'There is not information entered')

        return render(request, self.template_name, {'login_form': login_form})


class ForgetPasswordView(View):
    form_class = ForgetPasswordForm
    template_name = 'account/forget-password.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home-page')
        return super(ForgetPasswordView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        forget_pass = self.form_class()
        return render(request, self.template_name, {'forget_pass': forget_pass})

    def post(self, request):
        forget_pass = self.form_class(request.POST)
        if forget_pass.is_valid():
            email = forget_pass.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=email).first()
            if user:
                send_email('change password', user.email, {'user': user}, 'emails/forget-password.html')
                return redirect('account:login-page')

        return render(request, self.template_name, {'forget_pass': forget_pass})


class LogoutView(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        return redirect('account:login-page')


class ResetPasswordView(View):
    form_class = ResetPasswordForm
    template_name = 'account/reset-password.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home-page')
        return super(ResetPasswordView, self).dispatch(request, *args, **kwargs)

    def get(self, request, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect('account:login-page')

        reset_pass = self.form_class()

        return render(request, self.template_name, {'reset_pass': reset_pass})

    def post(self, request, active_code):
        reset_pass = self.form_class(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_pass.is_valid():
            if user is None:
                return redirect('account:login-page')
            new_user_pass = reset_pass.cleaned_data.get('password1')
            user.set_password(new_user_pass)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect('account:login-page')

        return render(request, self.template_name, {'reset_pass': reset_pass})
