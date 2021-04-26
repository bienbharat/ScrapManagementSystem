from __future__ import unicode_literals
from django.urls import path
from userPlus.views import signup
from userPlus.views.validate_user_name_apiview import ValidateUserName
from userPlus.views.register_company_view import companyDetails
from userPlus.views.company_profile import companyProfile
# from django.contrib.auth.views import auth_login as login


urlpatterns = [
    path('reg', signup.register, name='register'),
    path('activate/<uidb64>/<token>/', signup.activate, name='activate'),
    path('api/validateusername', ValidateUserName.as_view(), name='validateusername'),
    path('addcompanydetails', companyDetails, name='validateusername'),
    path('companyprofile', companyProfile, name='Company profile')
]

