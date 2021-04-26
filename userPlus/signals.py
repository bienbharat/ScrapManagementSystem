# from django.contrib.auth import signals
from django.dispatch import Signal


user_password_change = Signal(providing_args=['request', 'user'])
user_email_change = Signal(providing_args=['request', 'user', 'old_email', 'new_email'])
user_create = Signal(providing_args=['request', 'user'])
user_deactivate = Signal(providing_args=['request', 'user'])
user_activate = Signal(providing_args=['request', 'user'])

company_name_change = Signal(providing_args=['request', 'Company', 'old_name', 'new_name'])
