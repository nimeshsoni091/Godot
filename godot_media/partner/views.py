from django.shortcuts import render, redirect
from partner.forms import PartnerForm
from partner.models import Partners


# Create your views here.

def partner_list(request):
    context = {'partner_list': Partners.objects.all().order_by('-id')}
    return render(request, "partner_list.html", context)


def partner_form(request, id=0):
    # we are calling same function for GET and POST request
    if request.method == "GET":
        if id == 0:  # determines insert operation
            form = PartnerForm()
            operation = "insert"
        else:  # determines update operation and populate pre filled form
            partner = Partners.objects.get(pk=id)
            form = PartnerForm(instance=partner)
            operation = "update"
        return render(request, "partner_form.html", {'form': form, 'operation': operation})
    else:
        if id == 0:
            form = PartnerForm(request.POST)
        else:
            partner = Partners.objects.get(pk=id)
            form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            form.save()
        return redirect('/')
