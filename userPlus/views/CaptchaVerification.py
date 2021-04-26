from django.conf import settings
import urllib
import urllib.request as urllib2
import json

from django.conf import settings

def CaptchaVerification(request):
    recaptcha_response = request.POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    data = urllib.parse.urlencode(values).encode("utf-8")
    req = urllib2.Request(url)
    response = urllib2.urlopen(req, data=data)
    result = json.load(response)
    # print(data)
    # print(type(data))
    # print(req)
    # print(type(req))
    # print(response)
    # print(type(response))
    # print(result)
    # print(type(result))
    return result
