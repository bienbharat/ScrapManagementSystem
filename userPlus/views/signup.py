from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from userPlus.forms import UserCreationForm
from userPlus.models import User
from userPlus.views.CaptchaVerification import CaptchaVerification
from core import generate_uuid

UserModel = get_user_model()


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            verifyCaptcha = CaptchaVerification(request)
            print(verifyCaptcha)
            if verifyCaptcha['success']:
                user = form.save(commit=False)
                user.UserKey = generate_uuid()
                user.IsActive = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('signup_verify.html', {
                    'user': form,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                to_email = form.cleaned_data.get('EmailId')
                send_mail(mail_subject, message, 'bharats@bientechnologies.com', [to_email], fail_silently=False)
                return render(request, 'response.html')
            else:
                return HttpResponse("<h1> CAPTCHA VERIFICATION FAILED</h1>")
        else:
            form = UserCreationForm()
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        usr = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        usr = None
    if usr is not None and default_token_generator.check_token(usr, token):
        usr.is_active = True
        usr.is_emailVerified = True
        usr.save()
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')
