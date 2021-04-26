from userPlus.models import Company
from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict


@login_required(login_url="login")
def companyProfile(request):
    user = request.user
    if user is not None:
        # print(user)
        company = user.Company
        if company:
            dictonary = model_to_dict(company)
            return render(request, "Company_profile_page.html", {"form": dictonary})
        else:
            return redirect("/addcompanydetails")
    else:
        return HttpResponse("failed")