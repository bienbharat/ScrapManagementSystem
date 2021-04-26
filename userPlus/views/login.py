from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from userPlus.views.CaptchaVerification import CaptchaVerification
from web.webapp.helper_method import get_client_ip


def login_post(request):
    if request.method == 'POST':
        verifyCpatcha = CaptchaVerification(request)
        if verifyCpatcha['success']:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                user.LastLoginIP = get_client_ip(request)
                user.save()
                next_page = request.POST.get('next', "")
                if next_page is not None and len(next_page) > 0:
                    return redirect(next_page)
                else:
                    return redirect('products')
            else:
                return HttpResponse("<h3>Email or Password is incorrect</h3>")
        else:
            return HttpResponse("<h1>CAPTCHA VERIFICATION FAIL...</h1>")


def login_get(request):
    if request.user.is_authenticated:
        return redirect('products')
    return render(request, 'login.html', {'title': 'login'})


@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('homepage')


@login_required(login_url='login')
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            return HttpResponse('Please correctly enter your passwords...(:')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {'form': form})
