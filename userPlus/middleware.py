from __future__ import unicode_literals
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin


class TimezoneMiddelware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated() and request.user.Timezone:
            timezone.activate(request.user.Timezone)
        else:
            timezone.deactivate(user)