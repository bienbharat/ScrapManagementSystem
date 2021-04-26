from django.shortcuts import render, HttpResponse
from userPlus.forms import CompanyDetails

from businesslogic.services.company_service import add_company


def companyDetails(request):
    if request.method == 'POST':
        form = CompanyDetails(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['CompanyName']
            legal_name = form.cleaned_data['LegalName']
            pan_card = form.cleaned_data['PANCard']
            tax_id = form.cleaned_data['TaxID']
            username = form.cleaned_data['Username']
            mobile = form.cleaned_data['Mobile']
            address1 = form.cleaned_data['AddressLine1']
            address2 = form.cleaned_data['AddressLine2']
            locality = form.cleaned_data['Locality']
            city = form.cleaned_data['City']
            state = form.cleaned_data['State']
            country = form.cleaned_data['Country']
            postal_code = form.cleaned_data['PostalCode']

            add_company(company_name, legal_name, pan_card, tax_id,
                        username, mobile, address1, address2,
                        locality, city, state, country, postal_code)

            return render(request, 'success.html', {'success': "You have successfully added your Company details"})

        else:
            print(form.errors.as_data)
            return HttpResponse("error", status=200)
    else:
        form = CompanyDetails()
        return render(request, 'companydetailsform.html', {'form': form})